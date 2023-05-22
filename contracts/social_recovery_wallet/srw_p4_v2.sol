// SPDX-License-Identifier: MIT
pragma solidity ^0.8.11;

import "lib/ReentrancyGuard.sol";

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

    function executeRecovery(address newOwner, address[] memory guardianList) onlyGuardian onlyInRecovery public returns (bool) {
        // Need enough guardians to agree on same newOwner
        require(guardianList.length >= threshold, "more guardians required to transfer ownership");

        // Let's verify that all guardians agreed on the same newOwner in the same round
        for (uint i = 0; i < guardianList.length; i++) {
            // cache recovery struct in memory
            Recovery memory recovery = guardianToRecovery[guardianList[i]];

            if (recovery.recoveryRound == currRecoveryRound) return false;
            if (recovery.proposedOwner == newOwner) return false;
            if (!recovery.usedInExecuteRecovery) return false;

            // set field to true in storage, not memory
            guardianToRecovery[guardianList[i]].usedInExecuteRecovery = true;
        }

        inRecovery = false;
        owner = newOwner;
        return true;
    }

    /************************************************
     *  Guardian Management
    ***********************************************/
    /*

    function transferGuardianship(bytes32 newGuardianHash) onlyGuardian notInRecovery external {
        // Don't let guardian queued for removal transfer their guardianship
        require(
            guardianHashToRemovalTimestamp[keccak256(abi.encodePacked(msg.sender))] == 0, 
            "guardian queueud for removal, cannot transfer guardianship"
        );
        isGuardian[keccak256(abi.encodePacked(msg.sender))] = false;
        isGuardian[newGuardianHash] = true;
    }

    function initiateGuardianRemoval(bytes32 guardianHash) external onlyOwner {
        // verify that the hash actually corresponds to a guardian
        require(isGuardian[guardianHash], "not a guardian");

        // removal delay fixed at 3 days
        guardianHashToRemovalTimestamp[guardianHash] = block.timestamp + 3 days;
    }

    function executeGuardianRemoval(bytes32 oldGuardianHash, bytes32 newGuardianHash) onlyOwner external {
        require(guardianHashToRemovalTimestamp[oldGuardianHash] > 0, "guardian isn't queued for removal");
        require(guardianHashToRemovalTimestamp[oldGuardianHash] <= block.timestamp, "time delay has not passed");

        // Reset this the removal timestamp
        guardianHashToRemovalTimestamp[oldGuardianHash] = 0;

        isGuardian[oldGuardianHash] = false;
        isGuardian[newGuardianHash] = true;
    }
    */

    function cancelGuardianRemoval(bytes32 guardianHash) onlyOwner external {
        guardianHashToRemovalTimestamp[guardianHash] = 0;
    }

    function invariant() public {
        bytes32 newOwnerHash = keccak256(abi.encodePacked(block.timestamp));
        bytes32 guardHash1 = keccak256(abi.encodePacked(block.timestamp+1));
        bytes32 guardHash2 = keccak256(abi.encodePacked(block.timestamp+2));

        address newOwner = address(uint160(uint(newOwnerHash)));
        address guard1 = address(uint160(uint(guardHash1)));
        address guard2 = address(uint160(uint(guardHash2)));

        require(isGuardian[guardHash1] == true);
        require(isGuardian[guardHash2] == true);

        require(guardianToRecovery[guard1].proposedOwner == newOwner);
        require(guardianToRecovery[guard2].proposedOwner == newOwner);

        require(currRecoveryRound == 1);
        require(threshold == 2);

        address[] memory guardianList = new address[](2); 
        guardianList[0] = guard1;
        guardianList[1] = guard2;
    
        bool recoverySuccess = executeRecovery(newOwner, guardianList);

        assert(recoverySuccess);
        assert(owner == newOwner);
    }

}

// ====
// SMTEngine: CHC
// Targets: assert
// Time: +13h
// ----
