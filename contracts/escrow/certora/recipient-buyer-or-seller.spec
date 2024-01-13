rule recipient_buyer_or_seller {
    env e;
    
    redeem@withrevert(e);

    assert(!lastReverted =>
            (currentContract.recipient == getBuyer() ||
             currentContract.recipient == getSeller()));
}