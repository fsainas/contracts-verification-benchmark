rule P4 {
    uint index;
    address payee = getPayee(index);
    assert releasable(payee) <= getBalance();
}

