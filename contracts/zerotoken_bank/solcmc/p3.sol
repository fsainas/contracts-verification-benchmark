function invariant(ZeroTokenBank other, uint amount) public {
    try other.deposit(amount) {}
    catch {
        assert(false);
    }
}
