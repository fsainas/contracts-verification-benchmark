methods {
    function releasable() external returns (uint);
    function getBalance() external returns (uint) envfree;
    function getDuration() external returns (uint) envfree;
    function getStart() external returns (uint) envfree;
}

rule P4 {
    env e1;
    env e2;
    
    mathint releasable1 = releasable(e1);
    mathint balance1 = getBalance();
    mathint timestamp1 = e1.block.timestamp;

    mathint releasable2 = releasable(e2);
    mathint balance2 = getBalance();
    mathint timestamp2 = e2.block.timestamp;
    
    mathint start = getStart();

    require timestamp1 > start && timestamp2 > start;

    assert (
        timestamp2 > timestamp1 && 
        balance1 == balance2
        ) => releasable2 > releasable1;
}

rule NotP4 {
    env e1;
    env e2;
    
    mathint releasable1 = releasable(e1);
    mathint balance1 = getBalance();
    mathint timestamp1 = e1.block.timestamp;
    
    
    mathint releasable2 = releasable(e2);
    mathint balance2 = getBalance();
    mathint timestamp2 = e2.block.timestamp;
    
    mathint start = getStart();

    require timestamp1 > start && timestamp2 > start;

    assert (
        timestamp2 > timestamp1 && 
        balance1 == balance2
        ) => releasable2 < releasable1;
}

// V1 proof: https://prover.certora.com/output/49230/59a4a43b2af543aeb60d5c76cbface47?anonymousKey=425ba04ad36694c139257cfaa0b7352af63a74d4 