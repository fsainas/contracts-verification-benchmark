rule reveal_auth_owner {
    env e;
    string s;
    reveal(e, s);
    
    assert e.msg.sender == getOwner();
}
