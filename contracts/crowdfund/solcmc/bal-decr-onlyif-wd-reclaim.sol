function invariant(uint choice) public payable {
    require(block.number > end_donate);
    
    uint _balance = address(this).balance - msg.value;

    if (choice == 0) {
        donate();
    } else if (choice == 1) {
        withdraw();
    } else if (choice == 2) {
        reclaim();
    } else {
        require(false);
    }
    
    require(address(this).balance < _balance);
    assert(choice == 1 || choice == 2);
}
