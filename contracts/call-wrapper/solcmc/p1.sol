function invariant(address called) public {
    uint _balance = address(this).balance;
    callwrap(called);
    assert(_balance == address(this).balance);
}