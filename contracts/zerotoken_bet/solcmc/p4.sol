
// if B has at less than 1 token or he has already joined the bet yet, then he cannot deposit 1 token in the contract

function invariant() public {
    int old_balance_b = balance_b;
    int old_balance = balance;
    
    require (balance_b<1 || balance!=1);
    deposit();
    assert (balance_b==old_balance_b-1 && balance==old_balance);
}
