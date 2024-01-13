rule auth_in_dispute {
    env e;
    method f;
    calldataarg args;

    require f.selector != sig:getBalance().selector;
    require f.selector != sig:getBuyer().selector;
    require f.selector != sig:getSeller().selector;
    require f.selector != sig:getArbiter().selector;
    require f.selector != sig:getState().selector;
    
    require(getState() == Escrow.State.DISPUTE);
    f(e, args);
        
    assert (e.msg.sender == getArbiter());
}
