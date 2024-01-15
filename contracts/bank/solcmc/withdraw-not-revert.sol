function invariant(uint amount) public {
    require(amount <= balances[msg.sender]);
    
    (bool success, ) = address(this).call(abi.encodeWithSignature("withdraw(uint)", 1));
    assert(success);
}