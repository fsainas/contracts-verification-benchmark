# for_break_direct.sol
Produces the unreachable code warning on `++x`, but says nothing on the assert,
which can be false if `x != 0`.
