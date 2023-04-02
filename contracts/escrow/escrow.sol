// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Escrow {
    uint end_join;      // last block of the join phase
    uint end_choice;    // last block of the choice phase
    uint end_redeem;    // last block of the redeem phase

    uint fee_rate;      // fee_rate == 20 -> 0.20%

    address buyer;
    address seller;
    address escrow;
    uint deposit;       // buyer's deposit

    address buyer_choice;   // recipient of the deposit
    address seller_choice;  // recipient of the deposit
    address eChoice;        // choice of the escrow
    
    constructor (
        address _escrow, 
        uint _end_join, 
        uint _end_choice, 
        uint _end_redeem, 
        uint _fee_rate) {

        require(block.number < _end_join);
        require(_end_join < _end_choice);
        require(_end_choice < _end_redeem);

        require(_fee_rate <= 10000);    // The fee cannot be more then the deposit

        escrow = _escrow;
        end_join = _end_join;
        end_choice = _end_choice;
        end_redeem = _end_redeem;
        fee_rate = _fee_rate;
    }

    modifier beforeEndJoin() {
        require(block.number < end_join);
        _;
    }
    
    modifier beforeEndChoice() {
        require(block.number < end_choice);
        _;
    }

    modifier beforeEndReedem() {
        require(block.number < end_redeem);
        _;
    }

    modifier afterEndChoice() {
        require(block.number >= end_choice);
        _;
    }

    modifier afterEndReedem() {
        require(block.number >= end_redeem);
        _;
    }

    /*****************
          Join Phase
        *****************/
    function join(address _seller) public payable beforeEndJoin {

        require(msg.sender != _seller);
        buyer = msg.sender;
        seller = _seller;
        deposit = msg.value;
    }

    /*****************
         Choice Phase
        *****************/
    function choose(address _choice) public beforeEndChoice {

        require(msg.sender == buyer || msg.sender == seller);    // may be redundant

        if (msg.sender == seller && seller_choice == address(0)) {
            seller_choice = _choice;
        } else if (msg.sender == buyer && buyer_choice == address(0)) {
            buyer_choice = _choice;
        }
    }
 
    /*****************
         Redeem Phase 
        *****************/
    // The seller has not made a choice
    function redeem_without_seller() public afterEndChoice {

        require(msg.sender == buyer);
        require(seller_choice == address(0));

        deposit = 0;
        (bool success,) = buyer.call{value: deposit}("");      
        require(success);
    }
    
    function redeem() public afterEndChoice beforeEndReedem {

        require(msg.sender == seller);
        require(buyer_choice == seller_choice);
        require(block.number >= end_choice);

        deposit -= 0;
        (bool success,) = seller_choice.call{value: deposit}("");
        require(success);
    }

    /*****************
          Arbitrate
        *****************/
    function arbitrate(address _eChoice) public afterEndReedem {

        require(msg.sender == escrow);
        require(_eChoice == buyer_choice || _eChoice == seller_choice);
        require(eChoice != address(0));         // can choose only once
        
        eChoice = _eChoice;

        uint fee = deposit * (fee_rate / 10000);
        deposit -= fee;
        (bool success,) = escrow.call{value: fee}("");
        require(success);
    }

    function redeem_arbitrated() public {

        require(eChoice != address(0));

        deposit = 0;
        (bool success,) = eChoice.call{value: deposit}("");
        require(success);
    }

}
