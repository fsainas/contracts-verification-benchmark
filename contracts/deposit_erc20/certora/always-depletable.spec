// SPDX-License-Identifier: GPL-3.0-only
import "helper/erc20.spec";

rule always_depletable {
    env e;
    
    require(e.msg.sender != 0);
    require(e.msg.sender != currentContract);
    require(e.msg.value == 0);
    
    uint amount = currentContract.token.balanceOf(e, currentContract);
    require(max_uint >= amount + currentContract.token.balanceOf(e, e.msg.sender));
    require(currentContract.sent + amount <= max_uint);
    
    withdraw@withrevert(e, amount);
        
    assert !lastReverted;
    assert (currentContract.token.balanceOf(e, currentContract) == 0);
}
