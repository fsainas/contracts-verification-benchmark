//https://prover.certora.com/output/35919/fd0c7f0373384a98ac230f6c9719db7d?anonymousKey=9b85009960cb40290ce74050b119b0a5b564130f
import "helper/erc20.spec";
methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
    function getAddressBalance(address) external returns (uint) envfree;
    function getInitialDeposit() external returns (uint) envfree;
    function getSent() external returns (uint) envfree;
}
invariant wd_leq_init_bal()
    getSent() <= getInitialDeposit();
