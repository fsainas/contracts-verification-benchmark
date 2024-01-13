rule dispute_if_agree {
    env e;
    require (getState() == Escrow.State.AGREE);
    require (e.msg.sender == getBuyer() || 
             e.msg.sender == getSeller());
    require (e.msg.value == 0);
    
    open_dispute@withrevert(e);

    assert(!lastReverted);
}
