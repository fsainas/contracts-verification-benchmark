rule P4 {
    env e1;
    bool b1;
    if (b1) {
        finalize(e1);
    } else {
        cancel(e1);
    }
    
    env e2;
    bool b2;
    if (b2) {
        finalize@withrevert(e2);
    } else {
        cancel@withrevert(e2);
    }
    
    satisfy !lastReverted;
}
