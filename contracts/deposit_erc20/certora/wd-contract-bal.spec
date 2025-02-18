//https://prover.certora.com/output/35919/c8bc1868cc97446aab1205eea50afcc0?anonymousKey=954875f8a2ec1646d22abdf081550f399f0b7f4f
// SPDX-License-Identifier: GPL-3.0-only
import "./helper/erc20.spec";

rule wd_contract_bal {
    env e;
    uint amount;
    mathint mi_amount = amount;
    mathint before = getBalance(e);
    require before >= mi_amount;
    
    withdraw(e, amount);
    
    mathint after = getBalance(e);
    if(e.msg.sender == currentContract) {
        assert before == after;
    }
    else {
        assert before == after + mi_amount;
    }
}
