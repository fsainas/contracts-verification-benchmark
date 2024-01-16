rule commit_auth_owner {
    env e;
    bytes32 b;
    commit(e, b);
    
    assert e.msg.sender == getOwner();
}

// V1 proof: https://prover.certora.com/output/49230/89924abbcbb0413889015a33e2580975?anonymousKey=12a054681e4a6a3fcd46725079e7f81a97e3c58e
// V2 proof: https://prover.certora.com/output/49230/f7ef05f226ad4d7aa8d8624d53c5a197?anonymousKey=dcdfbadee5918a2889d6e00a0c283683b3d6a82c
// V3 proof: https://prover.certora.com/output/49230/317dae1c25f24457876e1b079cca6cd0?anonymousKey=2ab01c887629fee4292e95c4ad6dc9382d46c11b
// V4 proof: https://prover.certora.com/output/49230/57f8e53fbad44901ba0e8b51decdee62?anonymousKey=0cda976671145b9915f77ebbfc35103df0dfcdc3
