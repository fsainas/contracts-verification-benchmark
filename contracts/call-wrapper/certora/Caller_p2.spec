methods {
    function callyourself() external;
    function getData() external returns (uint) envfree;
}

rule P2 {
    env e;

    mathint before = getData();
    callyourself(e);
    mathint after = getData();

    assert before == after;
}

// V1 proof: https://prover.certora.com/output/49230/69997ddc1fcb4da890ab22a893836eb4?anonymousKey=539ca3d17857361999b405f5437cfb8fdda395d1
// V2 proof: https://prover.certora.com/output/49230/6d88452e7d6945bbaba166a78a114437?anonymousKey=8ece8e1dac5e63c0150f0109d8d6e7d8a5765433
// V3 proof: https://prover.certora.com/output/49230/e3dcfb149d224c869e20e4e22e840867?anonymousKey=dfa3dfc582eeaecc25a953350eb4be13339bb2a4
// V4 proof: https://prover.certora.com/output/49230/8806440359414f56acb1be8618a86286?anonymousKey=73616d59a066ed03bb2878dd6f170584ef7e32b8
// V5 proof: https://prover.certora.com/output/49230/7f0aa356e47c473fa7ecd9198f985934?anonymousKey=ab0932d59efd4787047f2a89163e141c54596576