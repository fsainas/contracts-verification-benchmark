function invariant() public view {
   assert(!_reveal_called || _reveal_sender==owner);
}
