// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract C {
    
    uint end_phase_1;
    uint end_phase_2;

    bool f_exec;
    bool g_exec;
    bool h_exec;

    constructor(uint _end_phase_1, uint _end_phase_2) {

        require(_end_phase_1 < _end_phase_2);

        end_phase_1 = _end_phase_1;
        end_phase_2 = _end_phase_2;

        f_exec = false;
        g_exec = false;
    }

    function f() public { 
        require(block.number < end_phase_1);
        f_exec = !f_exec;
    }

    function g() public { 
        require(block.number < end_phase_2);
        require(h_exec);
        g_exec = !g_exec;
    }

    function h() public {
        require(block.number >= end_phase_2);
        require(f_exec);
        h_exec = !h_exec;
    }

    function invariant() public view {
        assert(!(h_exec && !f_exec));       // h implies f
        assert(!g_exec);
    }
}

// ====
// SMTEngine: CHC
// Time: 1.97s
// ----
// Warning: CHC: Assertion violation happens here.
// Warning: CHC: Assertion violation happens here.
