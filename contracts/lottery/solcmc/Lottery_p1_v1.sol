// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.18;

contract Lottery {
    address[] private players;
    uint private start;
    uint private duration;

    constructor(uint duration_) {
        start = block.number;
        duration = duration_;
    }

    function enter() internal {
        //require(msg.value == .01 ether);
        assert(msg.value == .01 ether);
        
        players.push(msg.sender);
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encode(block.prevrandao)));
    }

    function pickWinner() public {
        require(block.number >= start + duration);

        address winner = players[random() % players.length];
        players = new address[](0);

        uint fee = address(this).balance / 100;

        start = block.number;

        (bool success,) = msg.sender.call{value: fee}("");
        require(success);

        (success,) = winner.call{value: address(this).balance}("");
        require(success);
    }

    function invariant() public payable {
        require(msg.value == .01 ether);

        enter();

        assert(players[players.length-1] == msg.sender);
    }

}
