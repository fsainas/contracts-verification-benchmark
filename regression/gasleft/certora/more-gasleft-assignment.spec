ghost mathint n;
ghost uint after_assignment;
ghost uint g;
hook GAS uint gas{
    if (n == 0) {
        g = gas;
    }
    else{
        after_assignment = gas;
    }
    n = n + 1;  
}
rule more_gasleft_assignment {
    env e;
    n = 0;
    g = 0;
    after_assignment = 0;
    f(e);
    assert(g < after_assignment);
}