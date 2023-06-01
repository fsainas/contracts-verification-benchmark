// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.18;

contract Lottery {
    address immutable private manager;
    address[] private players;

    constructor() {
        manager = msg.sender;
    }

    function enter() public payable {
        require(msg.value == .01 ether);
        
        players.push(msg.sender);
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encode(block.prevrandao)));
    }

    function pickWinner() public {
        require(msg.sender == manager);

        address winner = players[random() % players.length];
        players = new address[](0);

        (bool success,) = winner.call{value: address(this).balance}("");
        require(success);
    }

    function invariant() public payable {
        require(msg.value == .01 ether);

        enter();

        assert(players[players.length-1] == msg.sender);
    }

}
