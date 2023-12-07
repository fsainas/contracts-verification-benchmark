rule P1 {
    env e1;
    env e2;

    require e1.block.number < e2.block.number;

    mathint balance1 = getBalance(e1);
    mathint balance2 = getBalance(e2);

    assert balance1 >= balance2;
}
