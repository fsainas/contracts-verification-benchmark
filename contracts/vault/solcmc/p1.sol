function invariant_withdraw(address receiver, uint amount) public {
    withdraw(receiver, amount);
    assert(msg.sender == owner);
}

function invariant_finalize() public {
    finalize();
    assert(msg.sender == owner);
}
