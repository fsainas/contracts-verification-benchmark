rule P7 {
    env e;
    calldataarg args;
    method f;
    
    require(e.block.number > getEndDonate());
    require(f.selector != sig:getBalance().selector);
    require(f.selector != sig:getEndDonate().selector);
    require(f.selector != sig:getGoal().selector);
    require(f.selector != sig:donors(address).selector);
    
    f(e, args);

    assert f.selector == sig:reclaim().selector || f.selector == sig:withdraw().selector;
}


