//https://prover.certora.com/output/35919/ddf150a98e7b45d1993c1be9ef9bb869?anonymousKey=a20a1a34e8db04c56507a5ecd0fd31b5d8aac628
// SPDX-License-Identifier: GPL-3.0-only
import "helper/erc20.spec";

rule wd_not_revert {
    env e;
    uint amount;
    
    uint before = getAddressBalance(e, currentContract);
    require(e.msg.sender != 0);
    require(e.msg.value == 0);
    require(max_uint >= amount + getAddressBalance(e, e.msg.sender));
    require(currentContract.sent + amount + before <= max_uint);
    require(amount <= before);

    withdraw@withrevert(e, amount);
    assert !lastReverted;
}
