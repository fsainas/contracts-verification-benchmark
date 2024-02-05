function invariant(bool b, string memory s) public {
   require(!isCommitted);

   if (b) {
      reveal(s);
   } else {
      timeout();
   }

   assert(false);
}
