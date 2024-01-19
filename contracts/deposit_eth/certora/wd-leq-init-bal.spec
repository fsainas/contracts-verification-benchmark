// SPDX-License-Identifier: GPL-3.0-only

invariant wd_leq_init_bal()
    getSent() <= getInitialDeposit();
