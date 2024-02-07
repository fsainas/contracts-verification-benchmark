/// @custom:preghost function open_dispute
Escrow.State prev_state = state;

/// @custom:postghost function open_dispute
assert(prev_state==State.AGREE);
