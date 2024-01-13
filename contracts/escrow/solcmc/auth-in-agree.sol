function invariant_approve_payment() public {
    require(state==State.AGREE);
    approve_payment();
    assert(msg.sender == buyer || msg.sender == seller);
}

function invariant_refund() public {
    require(state==State.AGREE);
    refund();
    assert(msg.sender == buyer || msg.sender == seller);
}

function invariant_open_dispute() public {
    require(state==State.AGREE);
    open_dispute();
    assert(msg.sender == buyer || msg.sender == seller);
}
