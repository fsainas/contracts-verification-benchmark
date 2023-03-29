# Escrow 
This contract allows a buyer to deposit funds into an escrow account,
indicating the address of the seller. The buyer and seller can choose a payment
address, and if they match, the seller can redeem the funds. If they do not
match, the escrow system will arbitrate and choose the correct address between
the two. If the seller does not choose an address, the buyer can redeem the
funds after a set deadline. The contract operates in three phases: Join,
Choose, and Redeem. Each phase has a final block, and after that block the
functions of it can no longer be called.
