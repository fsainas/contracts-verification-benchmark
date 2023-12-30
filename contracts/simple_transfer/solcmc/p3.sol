function invariant(uint amount) public {
    uint prev_sender_balance = address(msg.sender).balance;
    withdraw(amount);
    uint sender_balance = address(msg.sender).balance;	
    assert(sender_balance == prev_sender_balance + amount);
}
