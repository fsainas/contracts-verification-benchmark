methods {
    function balanceOf(address) external returns (uint) envfree;
}

invariant inv()
    balanceOf(currentContract) == currentContract.initial;
