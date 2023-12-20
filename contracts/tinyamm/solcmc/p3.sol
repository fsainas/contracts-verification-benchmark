// if the last transaction was not a swap the supply has not changed

function invariant() public view {
    // should fail
    // assert(_prevSupply == supply);
    
        // should succeed
    assert(_lastTx!=Tx.Swap || _prevSupply == supply);
}
