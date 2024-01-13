function invariant_approve_payment() public {
    require(state==State.AGREE);
    uint prev_bal = address(this).balance;
    approve_payment();
    uint curr_bal = address(this).balance;
    assert(prev_bal==curr_bal);
}

function invariant_refund() public {
    require(state==State.AGREE);
    uint prev_bal = address(this).balance;
    refund();
    uint curr_bal = address(this).balance;
    assert(prev_bal==curr_bal);
}

function invariant_open_dispute() public {
    require(state==State.AGREE);
    uint prev_bal = address(this).balance;
    open_dispute();
    uint curr_bal = address(this).balance;
    assert(prev_bal==curr_bal);
}