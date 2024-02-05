// SPDX-License-Identifier: GPL-3.0-only

rule wd_not_revert {
    env e;
    uint amount;
    
    uint before = getAddressBalance(e.msg.sender);
    require e.msg.value == 0;
    require amount <= before;

    withdraw@withrevert(e, amount);
    assert !lastReverted;
}
