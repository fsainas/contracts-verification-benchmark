methods {
       function getStart() external returns (uint) envfree;
       function getOwner() external returns (address) envfree;
       function getIsCommitted() external returns (bool) envfree;
       function getBalance() external returns (uint);
       function commit(bytes32) external;
       function reveal(string) external;
       function timeout() external;
}

rule P4 {
    env e;
    bytes32 b;
    commit(e, b);
    
    assert e.msg.sender == getOwner();
}

rule NotP4 {
    env e;
    bytes32 b;
    commit(e, b);
    
    assert e.msg.sender != getOwner();
}

// V1 proof: https://prover.certora.com/output/49230/89924abbcbb0413889015a33e2580975?anonymousKey=12a054681e4a6a3fcd46725079e7f81a97e3c58e
// V2 proof: 
// V3 proof: 
// V4 proof: 
