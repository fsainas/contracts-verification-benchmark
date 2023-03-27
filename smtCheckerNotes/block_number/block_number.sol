// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract C {
    
    mapping(uint => uint) blockn;
    uint t_id;
    uint prev_t_id;

    uint end_phase_1;
    uint end_phase_2;

    bool f_exec;
    bool g_exec;
    bool h_exec;

    constructor(uint _end_phase_1, uint _end_phase_2) {

        require(_end_phase_1 < _end_phase_2);

        end_phase_1 = _end_phase_1;
        end_phase_2 = _end_phase_2;

        t_id = 0;
        blockn[t_id] = block.number;
    }

    modifier new_t() {
        prev_t_id = t_id;
        t_id += 1;
        uint rand = uint(keccak256(abi.encode(block.number))) % 2;
        blockn[t_id] = blockn[prev_t_id] + rand;         // could be the next block or the current one
        _;
    }

    function f() new_t public { 
        require(blockn[t_id] < end_phase_1);
        f_exec = !f_exec;
    }

    function g() new_t public { 
        require(blockn[t_id] < end_phase_2);
        require(h_exec);
        g_exec = !g_exec;
    }

    function h() new_t public {
        require(blockn[t_id] >= end_phase_2);
        require(f_exec);
        h_exec = !h_exec;
    }

    function invariant() public view {
        assert(blockn[t_id] >= blockn[prev_t_id]);
        assert(!(h_exec && !f_exec));       // h implies f
        assert(!g_exec);
    }
}

// ====
// SMTEngine: CHC
// time: 6.30s
// ----
