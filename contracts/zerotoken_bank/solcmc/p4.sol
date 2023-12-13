function invariant(ZeroTokenBank other, uint amount) public {
    require(amount <= other.balanceOf(msg.sender));
    
    try other.withdraw(amount) {}
    catch {
        assert(false);
    }
}
