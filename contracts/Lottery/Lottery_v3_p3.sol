// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.8.18;

contract Lottery {
    address[] private players;

    // ghost variables
    enum Call {ENTER, PICK}
    uint _prevPlayersLength;
    uint _playersLength;
    Call _lastCall;

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
        address winner = players[random() % players.length];
        players = new address[](0);

        uint fee = address(this).balance / 100;

        _prevPlayersLength = _playersLength;
        _playersLength = players.length;
        _lastCall = Call.PICK;

        (bool success,) = msg.sender.call{value: fee}("");
        require(success);

        (success,) = winner.call{value: address(this).balance}("");
        require(success);
    }

    function invariant() public view {
        // _lastCall != Call.PICK => _prevPlayersLength <= _playersLength
        assert(_lastCall == Call.PICK || _prevPlayersLength <= _playersLength);
    }

}
