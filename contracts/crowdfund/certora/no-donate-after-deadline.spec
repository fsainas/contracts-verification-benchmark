rule no_donate_after_deadline {
    env e;
        
    donate@withrevert(e);    
    assert lastReverted;
}


