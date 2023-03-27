// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract C {

    uint v;
    uint x;
    
    function f() public {
        v = uint(keccak256(abi.encode(block.number))) % 2;

        if (v == 0) { x = 1; }

        assert(x == 1 || x == 0);
        assert(x == 1);
        assert(x == 0);
    }

}
// ====
// SMTEngine: CHC
// ----
// Warning: CHC: Assertion violation happens here.
// Warning: CHC: Assertion violation happens here.
