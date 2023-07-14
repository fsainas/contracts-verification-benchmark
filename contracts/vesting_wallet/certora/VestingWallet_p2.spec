methods {
    function releasable() external returns (uint);
    function getBalance() external returns (uint) envfree;
    function getDuration() external returns (uint) envfree;
    function getStart() external returns (uint) envfree;
}

rule P2 {
    env e;
    mathint ending_timestamp = getStart() + getDuration();
    mathint current_timestamp = e.block.timestamp;
    require current_timestamp > ending_timestamp;
    assert releasable(e) == getBalance();
}

rule NotP2 {
    env e;
    mathint ending_timestamp = getStart() + getDuration();
    mathint current_timestamp = e.block.timestamp;
    assert ending_timestamp < current_timestamp => releasable(e) != getBalance();
}

// V1 proof: https://prover.certora.com/output/49230/9de7b066255c419ab010dc76086d75ef?anonymousKey=334520eb1e866143df92e3a64e54acf7e3e5a57a