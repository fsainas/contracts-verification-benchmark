// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Crowdfund {

    uint end_donate;    // last block in which users can donate
    uint goal;          // amount of ETH that must be donated for the crowdfunding to be succesful
    address receiver;   // receiver of the donated funds
    mapping(address => uint) public donors;

    // ghost variables
    enum Phase{D,       // donate
	       WR,      // withdraw or reclaim
	       R,       // reclaim
	       E        // end
    }
    enum Tx {  D,       // donate
	       W,       // withdraw
	       R        // reclaim
    }
    Phase _ph;
    Tx _tx;
    uint256 _balance;
    uint _blockn;       // current block number
    
    constructor (address payable receiver_, uint end_donate_, uint goal_) {
	require (goal_ > 0);
        receiver = receiver_;
	goal = goal_;
        end_donate = end_donate_;

        _blockn = block.number;
	_balance = address(this).balance;
	_ph = Phase.D;
    }

    function _delay(uint n) public {
    	_blockn = _blockn + n;
    }
    
    function donate() public payable {
        require (block.number <= end_donate);

    	if (_blockn>end_donate && _ph==Phase.D)
    	    _ph = Phase.WR;
	
        require (_ph == Phase.D);
        donors[msg.sender] += msg.value;
	_balance += msg.value;
	_tx = Tx.D;
    }

    function withdraw() public {
        require (block.number > end_donate);
        require (_ph == Phase.WR);	
        require (_balance >= goal);
	_balance = 0;	
        (bool succ,) = receiver.call{value: address(this).balance}("");
        require(succ);
	_ph = Phase.E;
	_tx = Tx.W;	
    }
    
    function reclaim() public {	
        require (block.number > end_donate);
        require (_ph == Phase.WR || _ph == Phase.R);
        require (_balance < goal || _balance - donors[msg.sender] >= goal);
        require (donors[msg.sender] > 0);
        uint amount = donors[msg.sender];
        donors[msg.sender] = 0;
	_balance -= amount;
	
        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);
	_ph = Phase.R;
	_tx = Tx.R;	
    }

    function invariant() public view {
	// _tx==D ==> _ph==D
	assert(_tx!=Tx.D || _ph==Phase.D);
	// _tx==W ==> _ph==WR
	assert(_tx!=Tx.W || _ph==Phase.WR);
	// _tx==R ==> _ph==WR || _ph==R
	assert(_tx!=Tx.R || _ph==Phase.WR || _ph==Phase.R);
    }
}
