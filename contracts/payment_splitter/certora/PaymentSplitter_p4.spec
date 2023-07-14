methods {
    function getPayee(uint) external returns(address) envfree;
    function getShares(address) external returns(uint) envfree;
    function releasable(address) external returns(uint) envfree;
    function getBalance() external returns(uint) envfree;
}

rule P4 {
    uint index;
    address payee = getPayee(index);
    assert releasable(payee) <= getBalance();
}

rule NotP4 {
    uint index;
    address payee = getPayee(index);
    assert releasable(payee) > getBalance();
}

// proof V1: https://prover.certora.com/output/49230/6f276f5929e04cfea0e895c22e24143e?anonymousKey=d015421564cebc30264e250f306748be3400c835
