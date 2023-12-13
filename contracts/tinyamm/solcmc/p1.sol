function invariant() public view {
    // strangely, this gives a violation:
    // require (ever_deposited);
    // assert (r0>0 && r1>0);
    
    // should succeed	
    assert (!ever_deposited || (r0>0 && r1>0));
}
