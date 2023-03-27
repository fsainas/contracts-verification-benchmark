// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract C {
    
    function f() public view {
        uint v = uint(keccak256(abi.encode(block.number))) % 2;

        assert(v == 0 || v == 1);
    }

}
// ====
// SMTEngine: CHC
// ----
