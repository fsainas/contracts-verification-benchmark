rule P3 {
    uint index;
    address payee = getPayee(index);
    assert getShares(payee) > 0;
}

