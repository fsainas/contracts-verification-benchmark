// the supply is strictly positive if a deposit has been made

rule P2 {
    assert currentContract.ever_deposited => currentContract.supply>0;
}
