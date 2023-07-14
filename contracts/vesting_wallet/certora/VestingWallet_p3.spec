methods {
    function releasable() external returns (uint);
    function getBalance() external returns (uint) envfree;
    function getDuration() external returns (uint) envfree;
    function getStart() external returns (uint) envfree;
}

rule P3 {
    env e;
    mathint start = getStart();
    mathint current_timestamp = e.block.timestamp;
    assert current_timestamp < start => releasable(e) == 0;
}

rule NotP3 {
    env e;
    mathint start = getStart();
    mathint current_timestamp = e.block.timestamp;
    assert current_timestamp < start => releasable(e) != 0;
}

// V1 proof: https://prover.certora.com/output/49230/d4cb3cd6ef0d4d579d32b8aafdd4fa55?anonymousKey=1e55d8d9f44e23bc64d675d16cba5c04b6954346