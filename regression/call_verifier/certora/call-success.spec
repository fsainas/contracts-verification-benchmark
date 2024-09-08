rule call_success {
    env e;
    address a;
    
    f(e, a);
    assert(currentContract.callSuccessful == true);
}