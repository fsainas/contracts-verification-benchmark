import "helper/erc20.spec";

rule deposit_deposit_revert {
    env e1;
    env e2;

    method f;
    calldataarg args;

    deposit(e1);
    f(e2, args);
    
    assert f.selector != sig:deposit().selector;
}

