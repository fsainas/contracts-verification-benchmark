methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
    function getAddressBalance(address) external returns (uint) envfree;
}

rule P3 {
    env e;
    uint amount;

    mathint before = getAddressBalance(e.msg.sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(e.msg.sender);
    
    //require(after <= before);

    assert after == before + amount;
}
