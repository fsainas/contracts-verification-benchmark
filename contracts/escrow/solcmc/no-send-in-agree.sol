function invariant(uint f,address dst) public {
    require(state==State.AGREE);
    uint prev_bal = address(this).balance;
    
    if (f==0)
        approve_payment();
    else if (f==1)
        refund();
    else if (f==2)
        open_dispute();
    else if (f==3)
        arbitrate(dst);
    else
        redeem();

    uint curr_bal = address(this).balance;
    assert(prev_bal==curr_bal);
}