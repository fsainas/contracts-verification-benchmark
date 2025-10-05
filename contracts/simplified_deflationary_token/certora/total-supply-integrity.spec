methods {
    function balanceOf(address account) external returns (uint256) envfree;
}

function balancesSum(env e, address owner, address receiver) returns mathint {
    mathint balancesSum;
    uint ownerBalance = 0;
    uint receiverBalance = 0;

    if(e.msg.sender != owner) {
        ownerBalance = balanceOf(owner);
    }
    if(e.msg.sender != receiver && owner != receiver) {
        receiverBalance = balanceOf(receiver);
    }
    balancesSum = balanceOf(e.msg.sender) + ownerBalance + receiverBalance;
    return balancesSum;
}
rule total_supply_integrity {
    env e;
    address owner = currentContract.owner;
    address receiver;
    address user;
    uint256 amount;
    mathint oldSumBalances = balancesSum(e, owner, receiver);
    uint256 oldUserBalance = balanceOf(user);

    requireInvariant correctTotalSupply;
    requireInvariant correctTransactionFeePercent;
    require(user != owner && user != receiver && user != e.msg.sender);
    require(oldSumBalances <= currentContract.totalSupply);
    transfer(e, receiver, amount);
    assert(balanceOf(user) == oldUserBalance);
    assert(balancesSum(e, owner, receiver) == oldSumBalances);
}


invariant correctTransactionFeePercent()
    currentContract.transactionFeePercent == 10;

invariant correctTotalSupply()
    currentContract.totalSupply == 1000000000000000000000000;