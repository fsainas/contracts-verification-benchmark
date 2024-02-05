rule commit_auth_owner {
    env e;
    bytes32 b;
    commit(e, b);
    
    assert e.msg.sender == getOwner();
}
