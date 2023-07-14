methods {
    function withdraw(uint) external;
    function getBalance() external returns (uint) envfree;
    function getAddressBalance(address) external returns (uint) envfree;
}

rule P3 {
    env e;
    uint amount;

    mathint before = getAddressBalance(e.msg.sender);
    withdraw(e, amount);
    mathint after = getAddressBalance(e.msg.sender);

    assert after == before + amount;
}

// V1 proof: https://prover.certora.com/output/49230/ae277a00105d479aa99b6dcc00ee57b6?anonymousKey=aceff97dfbb4d242a6edb53d281c2f3c0ee3fcdb
// V2 proof: https://prover.certora.com/output/49230/91561b12f89a4d58b7398d2f875fd726?anonymousKey=a87010dc8b1cad05ea9d6abfe304a6a1f96badc1
// V3 proof: https://prover.certora.com/output/49230/010c1bfdc25e4282a2a8d05da036a45b?anonymousKey=d4e9960b34a1b5f12049fc5ca084f2dad480380a
// V4 proof: https://prover.certora.com/output/49230/97c113bd9af84c1a905ce1ed99f3e3b5?anonymousKey=e4a11c39a1b1140f40f6d5d3dda0addfc39e5a98
// V5 proof: https://prover.certora.com/output/49230/f67d9480a9544e8fb414b87deb701481?anonymousKey=95ca0aa90369c7514e37e5e2ebeb4b00c30b5850