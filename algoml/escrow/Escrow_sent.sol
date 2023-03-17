// SPDX-License-Identifier: GPLv3
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
    uint sent;          // amout sent from this contract

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

    /*****************
          Join Phase
        *****************/
    function join(address _seller) public payable beforeEndJoin {

        require(msg.sender != _seller);
        buyer = msg.sender;
        seller = _seller;
        deposit = msg.value;

        assert(buyer != seller);        // Proven
    }

    /*****************
         Choice Phase
        *****************/
    function choose(address _choice) public beforeEndChoice {

        require(msg.sender == buyer || msg.sender == seller);    // may be redundant

        if (msg.sender == seller) {
            //require(seller_choice == address(0));       // Can choose only once
            seller_choice = _choice;
        } else if (msg.sender == buyer) {
            //require(buyer_choice == address(0));
            buyer_choice = _choice;
        }
    }
 
    /*****************
         Redeem Phase 
        *****************/
    function redeem() public beforeEndReedem {

        if (seller == address(0)) {          // if the seller has not joined
            require(block.number > end_join);
            (bool success,) = buyer.call{value: deposit}("");      
            require(success);
            sent += deposit;
            deposit -= deposit;
        }

        if (buyer_choice == seller_choice) {        // the transaction can proceed
            (bool success,) = seller_choice.call{value: deposit}("");
            require(success);
            sent += deposit;
            deposit -= deposit;
        }

    }

    /*****************
          Arbitrate
        *****************/
    function arbitrate(address _eChoice) public {

        require(msg.sender == escrow);
        require(_eChoice == buyer || _eChoice == seller);
        require(block.number > end_redeem);
        
        uint fee = deposit * fee_rate / 10000;
        (bool success,) = escrow.call{value: fee}("");
        require(success);
        sent += fee;
        deposit = deposit - fee;

        eChoice = _eChoice;
    }

    function redeem_arbitrated() public {

        require(eChoice != address(0));

        (bool success,) = eChoice.call{value: deposit}("");
        require(success);
        sent += deposit;
        deposit -= deposit;
    }

    function invariant() public view {
        assert(sent <= deposit);
    }
}
