// SPDX-License-Identifier: GPL-3.0-only

rule always_depletable {
    env e;
    require (e.msg.sender == e.tx.origin);
    uint amount = getAddressBalance(currentContract);
    withdraw(e, amount);
    
    assert (getAddressBalance(currentContract) == 0);
}
