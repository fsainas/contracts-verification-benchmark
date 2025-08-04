function balancesSum(address receiver) public view returns (uint256) {
   uint256 balanceSums;
   uint256 ownerBalance = 0;
   uint256 receiverBalance = 0;

   if(msg.sender != owner) {
       ownerBalance = balanceOf(owner);
   }
   if(msg.sender != receiver && owner != receiver) {
       receiverBalance = balanceOf(receiver);
   }
   balanceSums = balanceOf(msg.sender) + ownerBalance + receiverBalance;
   return balanceSums;
}

function totalSupplyIntegrity(address user, address receiver, uint256 amount) public {
   uint256 oldUserBalance = balanceOf(user);
   uint256 oldSumBalances = balancesSum(receiver);
   require(user != owner && user != receiver && user != msg.sender);
   require(oldSumBalances <= totalSupply);
   transfer(receiver, amount);
   assert(balanceOf(user) == oldUserBalance);
   assert(balancesSum(receiver) == oldSumBalances);
}
