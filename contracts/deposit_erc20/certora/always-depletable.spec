// SPDX-License-Identifier: GPL-3.0-only
import "helper/erc20.spec";

rule always_depletable {
    env e;
    
    require(e.msg.sender != 0);
    require(e.msg.sender != currentContract);
    require(e.msg.value == 0);
    
    uint amount = getAddressBalance(e, currentContract);
    require(max_uint >= amount + getAddressBalance(e, e.msg.sender));
    require(currentContract.sent + amount <= max_uint);
    withdraw@withrevert(e, amount);
        
    assert !lastReverted;
    assert (getAddressBalance(e, currentContract) == 0);
}
