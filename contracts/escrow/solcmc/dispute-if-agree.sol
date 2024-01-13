function invariant() public {
    require(state==State.AGREE);
    require(msg.sender==buyer || msg.sender==seller);

    (bool success, ) = address(this).call(abi.encodeWithSignature("open_dispute()", 1));
    assert(success);
}