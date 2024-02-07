/// @custom:preghost function donate
bool pre = block.number > end_donate;
 
/// @custom:postghost function donate
assert(!pre);
