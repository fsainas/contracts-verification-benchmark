rule P3 {
    env e;
    uint amount;

    mathint before = getAddressBalance(e.msg.sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(e.msg.sender);

    assert after == before + amount;
}
