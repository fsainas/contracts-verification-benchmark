function invariant() public {
    redeem();
    assert(recipient == buyer || recipient == seller);
}