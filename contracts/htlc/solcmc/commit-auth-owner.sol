function invariant(bytes32 s) public payable {
   commit(s);

   assert(msg.sender == owner);
}
