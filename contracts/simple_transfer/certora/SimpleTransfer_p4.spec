methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
    function getAddressBalance(address) external returns (uint) envfree;
}

rule P4 {
    env e;
    uint amount;

    uint before = getAddressBalance(e.msg.sender);
    require amount <= before;

    withdraw@withrevert(e, amount);

    uint after = getAddressBalance(e.msg.sender);
    
    assert !lastReverted;
}
