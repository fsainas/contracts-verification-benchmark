function getOwner() public view returns (address) {
   return owner;
}

function getBalance() public view returns (uint) {
   return address(this).balance;
}

function getStart() public view returns (uint) {
   return start;
}

function getIsCommitted() public view returns (bool) {
   return isCommitted;
}
