rule recipient_buyer_or_seller {
    env e;
    
    redeem(e);

    assert currentContract.recipient == getBuyer() || currentContract.recipient == getSeller();
}
