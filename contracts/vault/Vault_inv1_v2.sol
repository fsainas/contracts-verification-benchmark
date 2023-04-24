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
    mapping (uint => States) public _states;
    uint _last;
    
    constructor (address payable recovery_, uint wait_time_) payable {
        owner = msg.sender;
        recovery = recovery_;
        wait_time = wait_time_;
        state = States.IDLE;
        _last = 0;	
	_states[_last] = state;
    }

    receive() external payable { }

    //  IDLE -> REQ
    function withdraw(address receiver_, uint amount_) public {
        require(state != States.REQ);
        require(amount <= address(this).balance);
        require(msg.sender == owner);
        request_time = block.number;
        amount = amount_;
        receiver = receiver_;
        state = States.REQ;

        _last = _last+1;	
	_states[_last] = state;	
    }

    // REQ -> PAID
    function finalize() public { 
        require(state == States.REQ);
        require (block.number >= request_time + wait_time);
        require (msg.sender == owner);

        state = States.PAID;

        _last = _last+1;	
	_states[_last] = state;	
	
        (bool succ,) = receiver.call{value: amount}("");
        require(succ);
    }

    // REQ -> CANC
    function cancel() public {
        require(state == States.REQ);
        require (msg.sender == recovery);

        state = States.CANC;
        _last = _last+1;	
	_states[_last] = state;		
    }

   function invariant() public view {
       for (uint i=1; i<_last; i++) {
	   assert(_states[i-1] != _states[i]);
       }
   }       
}
