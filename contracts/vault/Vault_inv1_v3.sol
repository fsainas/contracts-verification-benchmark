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

    // ghost variables
    States _state;   
    States _prev;
    
    constructor (address payable recovery_, uint wait_time_) payable {
        owner = msg.sender;
        recovery = recovery_;
        wait_time = wait_time_;
        _state = States.IDLE;
        _prev = _state;	
    }

    receive() external payable { }

    //  IDLE,PAID,CANC -> REQ
    function withdraw(address receiver_, uint amount_) public {
        require(amount == 0);
	require(amount_ > 0);
        require(amount <= address(this).balance);
        require(msg.sender == owner);
        request_time = block.number;
        amount = amount_;
        receiver = receiver_;

        _prev = _state;		
        _state = States.REQ;
    }

    // REQ -> PAID
    function finalize() public { 
        require(amount > 0);
        require (block.number >= request_time + wait_time);
        require (msg.sender == owner);

        _prev = _state;		
        _state = States.PAID;
	uint to_send = amount;	
	amount = 0;

        (bool succ,) = receiver.call{value: to_send}("");
        require(succ);
    }

    // REQ -> CANC
    function cancel() public {
        require(amount > 0);
        require (msg.sender == recovery);
	amount = 0;
        _prev = _state;		
        _state = States.CANC;
    }

   function invariant() public view {
       // _prev = REQ => state in {PAID,CANC}
       assert(_prev != States.REQ ||
	      _state == States.PAID ||
	      _state == States.CANC);

       // _prev in {PAID,CANC} => state = REQ
       assert((_prev != States.PAID && _prev != States.CANC) ||
	      _state == States.REQ);
   }       
}
