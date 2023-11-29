//p1
 
    function invariant() public view {
        require(seller_choice != escrow && buyer_choice != escrow);

        assert(_msg_sender == escrow || 
               _msg_sender == buyer || 
               _msg_sender == seller);
    }
