rule sum_matches_array_values {
    env e;
    
    assert currentContract.sum == getSumOfValues(e);
}
