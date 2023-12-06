function invariant(uint amount) public {
    uint _prev_sender_balance = address(msg.sender).balance;
    withdraw(amount);
    uint _sender_balance = address(msg.sender).balance;	
    assert(_sender_balance == _prev_sender_balance + amount);
}
