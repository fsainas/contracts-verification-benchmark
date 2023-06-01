// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.18;

contract Lottery {
    address immutable private manager;
    address[] private players;
    mapping (address => bool) hasEntered;

    constructor() {
        manager = msg.sender;
    }

    function enter() external payable {
        require(msg.value == .01 ether);
        require(!hasEntered[msg.sender]);
        
        hasEntered[msg.sender] = true;
        players.push(msg.sender);
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encode(block.prevrandao)));
    }

    function pickWinner() public {
        require(msg.sender == manager);

        address winner = players[random() % players.length];

        assert(hasEntered[winner]);

        for (uint i = 0; i < players.length; i++) {
            hasEntered[players[i]] = false;
        }

        players = new address[](0);

        (bool success,) = winner.call{value: address(this).balance}("");
        require(success);
    }

}
