rule call_revert {
    env e;
    address a;
   
    f@withrevert(e, a);
    assert(lastReverted);
}