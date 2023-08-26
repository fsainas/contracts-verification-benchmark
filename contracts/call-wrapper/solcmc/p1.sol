function invariant() public {
    uint _balance = address(this).balance;
    callyourself();
    assert(_balance == address(this).balance);
}