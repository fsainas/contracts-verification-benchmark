import "helper/erc20.spec";

invariant wd_leq_init_bal()
    currentContract.sent <= currentContract.initial_deposit;
