function invariant() public view {
   assert(!_timeout_called || _timeout_diff > 1000);
}
