function invariant() public view {
    require(state == States.REQ);
    // assert(0 < amount);
    assert(amount <= address(this).balance);
}
