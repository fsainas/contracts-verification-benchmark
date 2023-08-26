function invariant() public {
    uint _data = data;
    callyourself();
    assert(_data == data);
}