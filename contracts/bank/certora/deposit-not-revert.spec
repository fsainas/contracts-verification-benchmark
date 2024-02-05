// SPDX-License-Identifier: GPL-3.0-only

rule deposit_not_revert {
    env e;

    require(e.msg.value <= balanceOf(e.msg.sender));
    deposit@withrevert(e);
    
    assert !lastReverted;
}
