// p4: if commit is called, then the sender must be the owner
function invariant() public view {
   assert(!isCommitted || _commit_sender==owner);
}
