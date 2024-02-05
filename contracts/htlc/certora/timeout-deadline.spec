rule timeout_deadline {
    env e;
    
    timeout(e);
    
    assert to_mathint(e.block.number) >= getStart() + 1000;
}
