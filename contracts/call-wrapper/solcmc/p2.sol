function invariant(address called) public {
    uint _data = data;
    callwrap(called);
    assert(_data == data);
}