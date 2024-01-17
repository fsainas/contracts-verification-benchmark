function invariant() public {
    require(address(this).balance < goal);
    
    withdraw();
    assert(false);
}
