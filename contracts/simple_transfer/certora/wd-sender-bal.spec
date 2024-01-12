rule wd_sender_bal {
    env e;
    uint amount;

    mathint before = getAddressBalance(e.msg.sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(e.msg.sender);

    assert after == before + amount;
}
