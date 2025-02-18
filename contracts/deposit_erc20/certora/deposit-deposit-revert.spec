//https://prover.certora.com/output/35919/1643cd466ef748dcb1119c2acecb8388?anonymousKey=7b21eac5d2a54593258a4f73b04d035ca4eceaf4
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

