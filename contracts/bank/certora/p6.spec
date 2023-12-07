rule P6 {
    env e;

    uint amount;
    
    require amount > getBalance(e.msg.sender);
    withdraw@withrevert(e, amount);
    
    assert lastReverted;
}
