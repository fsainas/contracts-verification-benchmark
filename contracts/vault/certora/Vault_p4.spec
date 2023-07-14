methods {
    function withdraw(address, uint) external;
    function finalize() external;
    function getOwner() external returns (address) envfree;
    function getState() external returns (Vault.States) envfree;
    function getAmount() external returns (uint) envfree;
    function getBalance() external returns (uint) envfree;
}

rule P4 {
    assert getState() == Vault.States.REQ => getAmount() <= getBalance();
}

rule NotP4 {
    assert getState() == Vault.States.REQ => getAmount() > getBalance();
}

// V1 proof: https://prover.certora.com/output/49230/26351b3305f94f2ea5094ad348ec9acb?anonymousKey=af3bccde046ab9cce7f11f24129768f93b259cda
// V2 proof: https://prover.certora.com/output/49230/ec1a0751a5a241e6b20590b73fb11447?anonymousKey=f4a159676d9dc18b4e7de8132c7b537840f18595
// V3 proof: https://prover.certora.com/output/49230/2520957625354c33ac6b9e1e94bb1fc4?anonymousKey=c6f4e0484f314cccdc5a204f16083e1880b0519a