// SPDX-License-Identifier: GPL-3.0-only
import "helper/erc20.spec";

rule wd_not_revert {
    env e;
    uint amount;
    uint before = currentContract.token.balanceOf(e, currentContract);
    
    require(e.msg.sender != 0);
    require(e.msg.value == 0);

    require(max_uint >= amount + currentContract.token.balanceOf(e, e.msg.sender));
    require(currentContract.sent + amount + before <= max_uint);
    require(amount <= before);

    withdraw@withrevert(e, amount);
    
    assert !lastReverted;
}
