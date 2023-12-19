function invariant(address receiver, uint amount, bool b) public {
    if (b) {
        withdraw(receiver, amount);
    } else {
        finalize();
    }
    assert(msg.sender == owner);
}
