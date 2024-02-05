uint saved;
bool done;

function invstore() public {
    require(block.number > end_donate);
    require(!done);

    saved = address(this).balance;
    done = true;
}

function invariant(uint choice) public {
    require(block.number > end_donate);
    require(done);

    assert(address(this).balance <= saved);
}
