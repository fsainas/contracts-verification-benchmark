methods {
    function withdraw(uint) external;
}

ghost initialDeposit() returns mathint;

hook Sstore address(this).balance uint256 totalBalance STORAGE {
    havoc initialDeposit;
}

rule P1 {
    env e;
}