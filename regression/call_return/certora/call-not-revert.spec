rule call_not_revert {
    env e;
    address a;
   
    f@withrevert(e, a);
    assert(!lastReverted);
}