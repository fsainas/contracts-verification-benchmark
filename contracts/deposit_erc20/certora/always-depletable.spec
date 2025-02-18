//https://prover.certora.com/output/35919/33a6aabe956f4719ad2b725fd710b671?anonymousKey=58e45d75635068ae5e49a00ce5b553d7f0536984
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
