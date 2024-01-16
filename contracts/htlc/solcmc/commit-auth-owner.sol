function invariant() public view {
   assert(!isCommitted || _commit_sender==owner);
}
