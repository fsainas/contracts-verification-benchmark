persistent ghost mathint deposit_counter {
    init_state axiom deposit_counter == 0;
}

hook Sstore ever_deposited bool value (bool old_value) { 
    deposit_counter = deposit_counter + 1;
}

invariant no_deposit_twice()
    deposit_counter <= 1;
