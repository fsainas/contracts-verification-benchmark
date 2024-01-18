// the contract balance is always nonnegative
    
//rule cb_gte0 {
//    assert getBalance()>=0;
//}

invariant cb_gte0()
    getBalance()>=0;

