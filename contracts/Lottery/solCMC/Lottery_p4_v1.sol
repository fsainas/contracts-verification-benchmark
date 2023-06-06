// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.18;

contract Lottery {
    address[] private players;
    uint private start;
    uint private duration;

    // ghost variables
    mapping (address => bool) _isPlayer; 

    constructor(uint duration_) {
        start = block.number;
        duration = duration_;
    }

    function enter() external payable {
        require(msg.value == .01 ether);
        
        players.push(msg.sender);
        _isPlayer[msg.sender] = true;
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encode(block.prevrandao)));
    }

    function pickWinner() public {
        require(block.number >= start + duration);

        address winner = players[random() % players.length];

        assert(_isPlayer[winner]);

        for (uint i = 0; i < players.length; i++) {
            _isPlayer[players[i]] = false;
        }

        players = new address[](0);

        uint fee = address(this).balance / 100;

        start = block.number;

        (bool success,) = msg.sender.call{value: fee}("");
        require(success);

        (success,) = winner.call{value: address(this).balance}("");
        require(success);
    }

}
