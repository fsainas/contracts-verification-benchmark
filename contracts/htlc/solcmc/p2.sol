// p2: if timeout or reveal are called, then commit must have been called
function invariant() public view {
   assert(!((_timeout_called || _reveal_called) && !_commit_called));
}
