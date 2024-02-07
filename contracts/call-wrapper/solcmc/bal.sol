/// @custom:preghost function callwrap
uint _balance = address(this).balance;

/// @custom:postghost function callwrap
assert(_balance == address(this).balance);
