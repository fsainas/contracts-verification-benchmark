// before the deadline, if B has at least 1 token and he has not joined the bet yet, 
// then he can deposit 1 token in the contract
    
function invariant() public {
    int old_balance_b = balance_b;

    require (block.number <= timeout_block);
    require (balance_b>=1 && balance==1);
    deposit();
    assert (balance_b==old_balance_b-1 && balance==2);
}
