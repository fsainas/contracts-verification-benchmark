function invariant(uint f,address dst) public {
    require(state==State.DISPUTE);
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
    assert(msg.sender == arbiter);
}