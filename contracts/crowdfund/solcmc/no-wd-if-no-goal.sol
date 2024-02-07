/// @custom:preghost function withdraw
require(address(this).balance < goal);

/// @custom:postghost function withdraw
assert(false);
