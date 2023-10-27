// p3: if timeout is called, then at least 1000 blocks have passed since
// the contract was deployed
function invariant() public view {
   assert(!_timeout_called || _timeout_diff > 1000);
}
