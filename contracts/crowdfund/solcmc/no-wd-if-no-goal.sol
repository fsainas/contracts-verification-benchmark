/// @custom:preghost function withdraw
bool pre = address(this).balance < goal;

/// @custom:postghost function withdraw
assert(!pre);
