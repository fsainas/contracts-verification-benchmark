// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

/// @custom:version conformant to specification.

contract Escrow {
   enum State {AGREE, DISPUTE, ARBITRATED, REDEEM, END}

    State state;

    address immutable buyer;
    address immutable seller;
    address immutable arbiter;
    uint immutable fee;
 
    modifier instate(State expected_state){         
        require(state == expected_state);
        _;
    }
 
    uint deposit;       // buyer's deposit
    address recipient;  // recipient agreed or chosen by the arbiter

    constructor (address seller_, address arbiter_, uint fee_) payable {
        require (seller_ != address(0) && arbiter_ != address(0));
        require(fee_ < msg.value);    // The fee cannot be more than the deposit

        buyer = msg.sender;
        seller = seller_;
        arbiter = arbiter_;
        fee = fee_;
        state = State.AGREE;
    }

    function approve_payment() instate(State.AGREE) public {
        require(msg.sender == buyer); 
        state = State.REDEEM;
        recipient = seller;      
    }

    function refund() instate(State.AGREE) public {
        require(msg.sender == seller);
        state = State.REDEEM;
        recipient = buyer;
    }

    function open_dispute() instate(State.AGREE) public {
        require(msg.sender == buyer || msg.sender == seller);
        state = State.DISPUTE;
    }

    function arbitrate(address dst) instate(State.DISPUTE) public {
        require(msg.sender == arbiter);
        require(dst == buyer || dst == seller);
    
        recipient = dst;
        state = State.REDEEM;
        deposit -= fee;

        (bool success,) = arbiter.call{value: fee}("");
        require(success);
    }

    function redeem() instate(State.REDEEM) public {
        state = State.END;
        (bool success,) = recipient.call{value: deposit}("");
        require(success);
    }
}
