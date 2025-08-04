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

rule liquidity {
    env e;
    address owner = currentContract.owner;
    uint amount;
    address receiver;

    requireInvariant correctTransactionFeePercent();
    requireInvariant correctTotalSupply();
    require(balancesSum(e, owner, receiver) <= currentContract.totalSupply);
    require(e.msg.value == 0);
    require(amount <= balanceOf(e.msg.sender) && amount > 0);

    bool isMoneyTransferred = transfer@withrevert(e, receiver, amount);
    assert(!lastReverted);
}

invariant correctTransactionFeePercent()
    currentContract.transactionFeePercent == 10;

invariant correctTotalSupply()
    currentContract.totalSupply == 1000000000000000000000000;