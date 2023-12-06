function invariant(uint amount) public {
    require(amount <= address(this).balance && amount >= 0);

    // ensures that the sender is a EOA
    require(msg.sender == tx.origin);	
        try this.withdraw(amount)  {
        } catch {
        // verification always fails	    
            assert(false);
        }

    // alternative encoding of p4 (verification always fails)
    // (bool success, ) = address(this).call(abi.encodeWithSignature("withdraw(uint)", 1));
    // assert(success);
}
