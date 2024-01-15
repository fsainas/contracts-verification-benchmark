rule withdraw_revert {
    env e;
    uint amount;

    require (amount==0 || amount>getBalance(e.msg.sender));

    withdraw@withrevert(e, amount);

    assert lastReverted;
}