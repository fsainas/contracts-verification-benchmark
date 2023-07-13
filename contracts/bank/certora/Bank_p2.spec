methods {
    function getBalance(address) external returns(uint) envfree;
    function getContractBalance() external returns (uint) envfree;
    function withdraw(uint) external;
}

rule P2 {
    env e;
    method receive;
    calldataarg args;

    address sender = e.msg.sender;
    
    uint256 senderBalanceBefore = getBalance(sender);

    receive(e, args);

    uint256 senderBalanceAfter = getBalance(sender);

    assert e.msg.value > 0 <=> senderBalanceBefore < senderBalanceAfter;
}

// V1 proof: https://prover.certora.com/output/49230/7328b497ed51422ab5813b1240eec3c5?anonymousKey=6617191fc7515f0ecdb47f268a89da3a98330270
// V2 proof: https://prover.certora.com/output/49230/584ef6b3727a4acf92b68d97b29315d6?anonymousKey=e9726050ef9612b0aafafa6c66c849b46c9f80dd
// V3 proof: https://prover.certora.com/output/49230/d449ac12cb2047e0812b6efa1e33cb08?anonymousKey=800772959ac2b236deb4032e6225c02e827c1931