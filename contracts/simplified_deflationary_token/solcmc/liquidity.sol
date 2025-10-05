function liquidity(address receiver, uint256 amount) public {
    require(balancesSum(receiver) <= totalSupply);
    require(amount <= balanceOf(msg.sender) && amount > 0);
    bool isMoneyTransferred = transfer(receiver, amount);
    assert(isMoneyTransferred);
}

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