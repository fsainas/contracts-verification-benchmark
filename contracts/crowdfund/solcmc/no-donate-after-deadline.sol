function invariant() public {
    require(block.number > end_donate);

    donate();
    assert(false);
}