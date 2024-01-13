rule dispute_onlyif_agree {
    env e;

    Escrow.State s = getState();

    open_dispute@withrevert(e);

    assert(!lastReverted => s == Escrow.State.AGREE);
}