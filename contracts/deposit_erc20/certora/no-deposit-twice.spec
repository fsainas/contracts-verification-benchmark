persistent ghost bool multiple_deposit {
    init_state axiom multiple_deposit == false;
}

hook Sstore ever_deposited bool value (bool old_value) { 
    if(old_value && value)
        multiple_deposit = true;
}

invariant no_deposit_twice()
    !multiple_deposit;