function invariant(uint choice, uint u1, address a) public payable {
    uint currb = balances[a];
    if (choice == 0) {
        deposit();
    } else if (choice == 1) {
        withdraw(u1);
    } else {
        require(false);
    }
    uint newb = balances[a];

    require(newb < currb);
    assert(choice == 1);
    assert(msg.sender == a);
}
