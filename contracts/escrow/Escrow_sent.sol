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
    uint init_deposit;
    uint sent;          // amout sent from this contract

    uint blocknum;

    enum Phase {JOIN, CHOICE1, CHOICE2, REDEEM, END}

    Phase phase;

    address buyer_choice;   // recipient of the deposit
    address seller_choice;  // recipient of the deposit
    address eChoice;        // choice of the escrow
    
    constructor (
        address _escrow, 
        //uint _end_join, 
        //uint _end_choice, 
        //uint _end_redeem, 
        uint _fee_rate) {

            /*
        require(block.number < _end_join);
        require(_end_join < _end_choice);
        require(_end_choice < _end_redeem);
        */

        require(_fee_rate <= 10000);    // The fee cannot be more then the deposit

        escrow = _escrow;
        /*
        end_join = _end_join;
        end_choice = _end_choice;
        end_redeem = _end_redeem;
        */
        fee_rate = _fee_rate;

        phase = Phase.JOIN;
    }

    /*
    modifier beforeEndJoin() {
        //require(blocknum < end_join);
        require(phase == Phase.JOIN);
        _;
    }
    
    modifier beforeEndChoice() {
        //require(blocknum < end_choice);
        require(phase == Phase.CHOOSE);
        _;
    }

    modifier beforeEndReedem() {
        //require(blocknum < end_redeem);
        require(phase == Phase.REDEEM);
        _;
    }

    modifier afterEndReedem() {
        //require(blocknum > end_redeem);
        _;
    }
    */
     
    modifier nonZeroSender() {
        require(msg.sender != address(0));  // this should probably be a default assumption
        _;
    }
    

    /*****************
          Join Phase
        *****************/
    function join(address _seller) public payable /*beforeEndJoin*/ nonZeroSender {

        require(phase == Phase.JOIN);

        require(msg.sender != _seller);
        buyer = msg.sender;
        seller = _seller;
        deposit = msg.value;
        init_deposit = msg.value;
        require(init_deposit == deposit);

        phase = Phase.CHOICE1;
    }

    /*****************
         Choice Phase
        *****************/
    function choose(address _choice) public /*beforeEndChoice*/ {

        require(phase == Phase.CHOICE1 || phase == Phase.CHOICE2);

        require(msg.sender == buyer || msg.sender == seller);    // may be redundant

        if (msg.sender == seller && seller_choice == address(0)) {
            //require(seller_choice == address(0));       // Can choose only once
            seller_choice = _choice;
            if(phase == Phase.CHOICE1) phase = Phase.CHOICE2;
            else phase = Phase.REDEEM;
        } else if (msg.sender == buyer && seller_choice == address(0)) {
            //require(buyer_choice == address(0));
            buyer_choice = _choice;
            if(phase == Phase.CHOICE1) phase = Phase.CHOICE2;
            else phase = Phase.REDEEM;
        }
    }
 
    /*****************
         Redeem Phase 
        *****************/
    function redeem() public /*beforeEndReedem*/ nonZeroSender {

        require(phase == Phase.REDEEM);
        require(msg.sender == seller || msg.sender == buyer);

        if (seller_choice == address(0)) {          // if the seller has not choosen
            //require(block.number > end_join);
            uint amount = deposit;
            deposit -= amount;
            sent += amount;
            //(bool success,) = buyer.call{value: amount}("");      
            /*
            bool success = true;
            if (!success) {
                deposit += amount;
                sent -= amount;
            }
            */
            //require(success);
            phase = Phase.END;
        }

        if (buyer_choice == seller_choice) {        // the transaction can proceed
            uint amount = deposit;
            deposit -= amount;
            sent += amount;
            //(bool success,) = seller_choice.call{value: amount}("");
            /*
            bool success = true;
            if (!success) {
                deposit += amount;
                sent -= amount;
            }
            */
            //require(success);
            phase = Phase.END;
        }

    }

    /*****************
          Arbitrate
        *****************/
    function arbitrate(address _eChoice) public /*afterEndReedem*/ {

        require(msg.sender == escrow);
        require(_eChoice == buyer_choice || _eChoice == seller_choice);
        
        uint fee = deposit * fee_rate / 10000;
        deposit -= fee;
        sent += fee;
        //(bool success,) = escrow.call{value: fee}("");
        /*
        bool success = true;
        if (!success) {
            deposit += fee;
            sent -= fee;
        }
        */
        //require(success);

        eChoice = _eChoice;
    }

    function redeem_arbitrated() public {

        require(eChoice != address(0));

        uint amount = deposit;
        deposit -= amount;
        sent += amount;
        //(bool success,) = eChoice.call{value: amount}("");
        /*
        bool success = true;
        if (!success) {
            deposit += amount;
            sent -= amount;
        }
        */
        //require(success);
    }

    function invariant() public view {
        assert(sent <= init_deposit);
    }
}
