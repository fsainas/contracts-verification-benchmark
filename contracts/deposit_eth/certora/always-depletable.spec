// SPDX-License-Identifier: GPL-3.0-only

rule always_depletable {
    env e;
    require (e.msg.sender == e.tx.origin);
    uint amount = getAddressBalance(currentContract);
    withdraw@withrevert(e, amount);
    
    assert !lastReverted;
    assert (getAddressBalance(currentContract) == 0);
}
