function invariant(string memory s) public {
   reveal(s);

   assert(msg.sender == owner);
}
