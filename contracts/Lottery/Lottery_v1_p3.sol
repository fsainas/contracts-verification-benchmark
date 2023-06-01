// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.18;

contract Lottery {
    address immutable private manager;
    address[] private players;

    // ghost variables
    enum Call {ENTER, PICK}
    uint _prevPlayersLength;
    uint _playersLength;
    Call _lastCall;

    constructor() {
        manager = msg.sender;
    }

    function enter() external payable {
        require(msg.value == .01 ether);
        
        players.push(msg.sender);

        _prevPlayersLength = _playersLength;
        _playersLength = players.length;
        _lastCall = Call.ENTER;
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encode(block.prevrandao)));
    }

    function pickWinner() public {
        require(msg.sender == manager);

        address winner = players[random() % players.length];
        players = new address[](0);

        _prevPlayersLength = _playersLength;
        _playersLength = players.length;
        _lastCall = Call.PICK;

        (bool success,) = winner.call{value: address(this).balance}("");
        require(success);
    }

    function invariant() public view {
        // _lastCall != Call.PICK => _prevPlayersLength <= _playersLength
        assert(_lastCall == Call.PICK || _prevPlayersLength <= _playersLength);
    }

}
