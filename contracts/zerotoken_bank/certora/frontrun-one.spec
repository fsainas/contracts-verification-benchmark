rule P17 {
    storage initial = lastStorage;

    method f;
    env e1;
    calldataarg args1;
    f@withrevert(e1, args1) at initial;
    uint balance1 = balanceOf(e1.msg.sender);

    method g;
    env e0;
    calldataarg args0;
    require e0.msg.sender != e1.msg.sender;
    g(e0, args0) at initial;
    f@withrevert(e1, args1);
    uint balance2 = balanceOf(e1.msg.sender);

    assert balance1 == balance2;
}

