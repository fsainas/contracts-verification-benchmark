function invariant_arbitrate(address dst) public {
    require(state==State.DISPUTE);
    arbitrate(dst);
    assert(msg.sender == arbiter);
}

function invariant_approve_payment() public {
    require(state==State.DISPUTE);
    approve_payment();
    assert(msg.sender == arbiter);
}

function invariant_refund() public {
    require(state==State.DISPUTE);
    refund();
    assert(msg.sender == arbiter);
}

function invariant_open_dispute() public {
    require(state==State.DISPUTE);
    open_dispute();
    assert(msg.sender == arbiter);
}
