rule call_failure {
    env e;
    address a;
    
    f(e, a);
    assert(currentContract.callSuccessful == false);
}