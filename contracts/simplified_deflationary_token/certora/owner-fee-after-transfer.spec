methods {
    function balanceOf(address account) external returns (uint256) envfree;
    function calculateFee(uint256 amount) external returns (uint256) envfree;
}


rule owner_fee_after_transfer {
    env e;
    address owner = currentContract.owner;
    address receiver;

    uint256 amount;
    require(amount > 0);
    require(currentContract.isExcludedFromFee[e.msg.sender] == false);

    uint256 fee = calculateFee(amount);

    assert(fee > 0);
}