// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Escrow {
    enum Phase {JOIN, CHOICE, REDEEM}

    Phase phase;

    uint fee_rate;      // fee_rate == 20 -> 0.20%

    address buyer;
    address seller;
    address escrow;

    uint deposit;       // buyer's deposit

    address buyer_choice;       // recipient of the deposit
    address seller_choice;      // recipient of the deposit
    address escrow_choice;      // choice of the escrow

    constructor (
        address escrow_, 
        uint fee_rate_) {

        require(fee_rate_ <= 10000);    // The fee cannot be more than the deposit

        escrow = escrow_;
        fee_rate = fee_rate_;

        phase = Phase.JOIN;
    }

    modifier phaseJoin() {
        require(phase == Phase.JOIN);
        _;
    }
    
    modifier phaseChoice() {
        require(phase == Phase.CHOICE);
        _;
    }

    modifier phaseRedeem() {
        require(phase == Phase.REDEEM);
        _;
    }

    /*****************
          Join Phase
        *****************/
    function join(address seller_) public payable phaseJoin {

        require(msg.sender != seller_);

        buyer = msg.sender;
        seller = seller_;
        deposit = msg.value;

        phase = Phase.CHOICE;
    }

    /*****************
         Choice Phase
        *****************/
    function choose(address choice) public phaseChoice {

        if (msg.sender == seller && seller_choice == address(0)) {
            seller_choice = choice;
            if (buyer_choice != address(0)) phase = Phase.REDEEM;
        } else if (msg.sender == buyer && buyer_choice == address(0)) {
            buyer_choice = choice;
            if (seller_choice != address(0)) phase = Phase.REDEEM;
        }
    }

    function refund() public phaseChoice {

        require(msg.sender == buyer);
        require(seller_choice == address(0));

        deposit = 0;
        (bool success,) = buyer.call{value: deposit}("");      
        require(success);
    }
 
    /*****************
         Redeem Phase 
        *****************/
    
    function redeem() public phaseRedeem {

        require(msg.sender == seller);
        require(buyer_choice == seller_choice);

        deposit = 0;
        (bool success,) = seller_choice.call{value: deposit}("");
        require(success);
    }

    /*****************
          Arbitrate
        *****************/
    function arbitrate(address escrow_choice_) public phaseRedeem {

        require(msg.sender == escrow);
        require(escrow_choice_ == buyer_choice || escrow_choice_ == seller_choice);
        require(escrow_choice_ != address(0));         // can choose only once
        
        escrow_choice = escrow_choice_;

        uint fee = deposit * (fee_rate / 10000);
        deposit -= fee;
        (bool success,) = escrow.call{value: fee}("");
        require(success);
    }

    function redeem_arbitrated() public phaseRedeem {

        require(escrow_choice != address(0));

        deposit = 0;
        (bool success,) = escrow_choice.call{value: deposit}("");
        require(success);
    }

}
