function invariant() public view {
    // should fail
    // assert(_prevSupply == supply);
    
        // should succeed
    assert(_lastTx!=Tx.Swap || _prevSupply == supply);
}
