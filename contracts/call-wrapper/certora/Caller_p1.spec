methods {
    function callyourself() external;
    function getBalance() external returns (uint) envfree;
}

rule P1 {
    env e;

    mathint before = getBalance();
    callyourself(e);
    mathint after = getBalance();

    assert before == after;
}

// V1 proof: https://prover.certora.com/output/49230/88acbee6df954b579f6ef18deb56c870?anonymousKey=76ee36a772c6dc82ed7d8a6fde91f78ea975d45c
// V2 proof: https://prover.certora.com/output/49230/ead0d502b00a47d295b4da2169e69841?anonymousKey=88cd5e94c859ab75f5e31dde2211fe5f98452f35
// V3 proof: https://prover.certora.com/output/49230/29f2822de0aa42edbbcff40bc82299b1?anonymousKey=842bb0a3c38aabecbc32a6ca9fbe71a8f4424f82
// V4 proof: https://prover.certora.com/output/49230/4ace1534f8204e87a43e77a9d4321596?anonymousKey=154ae000ffe057820a39d781e55447c510e2edff
// V5 proof: https://prover.certora.com/output/49230/3641c94d010f40fd8fcc99b074c9b7c2?anonymousKey=b3a70869c586a49b821623d431ef81f0b05189f4