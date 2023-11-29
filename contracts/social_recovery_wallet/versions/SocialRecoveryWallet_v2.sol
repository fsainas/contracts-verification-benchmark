// SPDX-License-Identifier: MIT
pragma solidity ^0.8.11;

import "./lib/ReentrancyGuard.sol";


/// @custom:version removed guardian management
contract Wallet is ReentrancyGuard {

    // hash of guardian address
    mapping(bytes32 => bool) public isGuardian;
    uint256 public threshold;
    address public owner;
    bool public inRecovery;
    uint256 public currRecoveryRound;
    mapping(bytes32 => uint256) public guardianHashToRemovalTimestamp;

    /// @notice struct used for bookkeeping during recovery mode
    /// @dev trival struct but can be extended in future (when building for malicious guardians
    /// or when owner key is compromised)
    struct Recovery {
        address proposedOwner;
        uint256 recoveryRound; // recovery round in which this recovery struct was created
        bool usedInExecuteRecovery; // set to true when we see this struct in RecoveryExecute
    }

    mapping(address => Recovery) public guardianToRecovery;
    
    // ghost variables
    address _first_owner;
    
    /************************************************
     *  MODIFIERS 
    ***********************************************/

    modifier onlyOwner {
        require(msg.sender == owner, "only owner");
        _;
    }

    modifier onlyGuardian {
        require(isGuardian[keccak256(abi.encodePacked(msg.sender))], "only guardian");
        _;
    }

    modifier notInRecovery {
        require(!inRecovery, "wallet is in recovery mode");
        _;
    }

    modifier onlyInRecovery {
        require(inRecovery, "wallet is not in recovery mode");
        _;
    }

    constructor(bytes32[] memory guardianAddrHashes, uint256 threshold_) {
        require(threshold_ <= guardianAddrHashes.length, "threshold too high");
        
        for(uint i = 0; i < guardianAddrHashes.length; i++) {
            require(!isGuardian[guardianAddrHashes[i]], "duplicate guardian");
            isGuardian[guardianAddrHashes[i]] = true;
        }
        
        threshold = threshold_;
        owner = msg.sender;
        //variabile presa dal file creato dal makefile nel repo
        _first_owner = owner;
    }

    function executeExternalTx(address callee, 
        uint256 value, 
        bytes memory data
    ) external onlyOwner nonReentrant returns (bytes memory) {
        (bool success, bytes memory result) = callee.call{value: value}(data);
        require(success, "external call reverted");
        return result;
    }

    /************************************************
     *  Recovery
    ***********************************************/

    function initiateRecovery(address _proposedOwner) onlyGuardian notInRecovery external {
        // we are entering a new recovery round
        currRecoveryRound++;
        guardianToRecovery[msg.sender] = Recovery(
            _proposedOwner,
            currRecoveryRound, 
            false
        );
        inRecovery = true;
    }

    function supportRecovery(address _proposedOwner) onlyGuardian onlyInRecovery external {
        guardianToRecovery[msg.sender] = Recovery(
            _proposedOwner,
            currRecoveryRound, 
            false
        );
    }

    function cancelRecovery() onlyOwner onlyInRecovery external {
        inRecovery = false;
    }

    function executeRecovery(address newOwner, address[] calldata guardianList) onlyGuardian onlyInRecovery external {
        // Need enough guardians to agree on same newOwner
        require(guardianList.length >= threshold, "more guardians required to transfer ownership");

        // Let's verify that all guardians agreed on the same newOwner in the same round
        for (uint i = 0; i < guardianList.length; i++) {
            // cache recovery struct in memory
            Recovery memory recovery = guardianToRecovery[guardianList[i]];

            require(recovery.recoveryRound == currRecoveryRound, "round mismatch");
            require(recovery.proposedOwner == newOwner, "disagreement on new owner");
            require(!recovery.usedInExecuteRecovery, "duplicate guardian used in recovery");

            // set field to true in storage, not memory
            guardianToRecovery[guardianList[i]].usedInExecuteRecovery = true;
        }


        inRecovery = false;
        owner = newOwner;
    }

}
