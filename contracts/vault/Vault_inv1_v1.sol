// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Vault {
    enum States{IDLE, REQ, PAID, CANC}

    address owner;
    address recovery;
    uint wait_time;

    address receiver;
    uint request_time;
    uint amount;
    States state;

    // ghost variables
    States _prev;
    
    constructor (address payable recovery_, uint wait_time_) payable {
        owner = msg.sender;
        recovery = recovery_;
        wait_time = wait_time_;
        state = States.IDLE;
        _prev = state;	
    }

    receive() external payable { }

    //  IDLE,PAID,CANC -> REQ
    function withdraw(address receiver_, uint amount_) public {
        require(state != States.REQ);
        require(amount <= address(this).balance);
        require(msg.sender == owner);
        request_time = block.number;
        amount = amount_;
        receiver = receiver_;
        _prev = state;		
        state = States.REQ;
    }

    // REQ -> PAID
    function finalize() public { 
        require(state == States.REQ);
        require (block.number >= request_time + wait_time);
        require (msg.sender == owner);

        _prev = state;		
        state = States.PAID;	
	
        (bool succ,) = receiver.call{value: amount}("");
        require(succ);
    }

    // REQ -> CANC
    function cancel() public {
        require(state == States.REQ);
        require (msg.sender == recovery);
        _prev = state;		
        state = States.CANC;
    }

   function invariant() public view {
       // _prev = REQ => state in {PAID,CANC}
       assert(_prev != States.REQ ||
	      state == States.PAID ||
	      state == States.CANC);

       // _prev in {PAID,CANC} => state = REQ
       assert((_prev != States.PAID && _prev != States.CANC) ||
	      state == States.REQ);
   }       
}
