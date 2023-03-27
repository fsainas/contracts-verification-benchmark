// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract C {
    
    bool f_exec;
    bool g_exec;

    function f() public { 
        f_exec = true;
    }

    function g() public { 
        require(f_exec);
        g_exec = true;
    }

    function invariant() public view {
        assert(!(!f_exec && g_exec));       // g implies f
    }
}
// ====
// SMTEngine: CHC
// Time: 0.04s
// ----
