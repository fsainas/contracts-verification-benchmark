rule no_send_in_agree {
    env e;
    method f;
    calldataarg args;

    require(getState() == Escrow.State.AGREE);

    mathint old_balance = getBalance();        
    f(e, args);
    mathint new_balance = getBalance();

    assert(old_balance == new_balance);
}