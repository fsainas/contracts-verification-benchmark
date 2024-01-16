function invariant() public view {
   // assert(!((_timeout_called || _reveal_called) && !_commit_called));
   assert(!(_timeout_called || _reveal_called) || _commit_called);
}
