//p3

    function invariant() public {
        require(block.number > end_donate);

        _prevBalance = _balance;
        _balance = address(this).balance;

        assert(!(_prevBalance != 0) || _prevBalance >= _balance);
    }
