// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract Crowdfund {

    uint end_donate;    // last block in which users can donate
    uint goal;          // amount of ETH that must be donated for the crowdfunding to be succesful
    address receiver;   // receiver of the donated funds
    mapping(address => uint) public donors;

    // ghost variables
    enum Tx{I,D,W,R}
    Tx _tx1;            // previous tx
    Tx _tx2;            // last tx
    uint256 _balance;
    uint _blockn;       // current block number
    
    constructor (address payable receiver_, uint end_donate_, uint goal_) {
	require (goal_ > 0);
        receiver = receiver_;
	goal = goal_;
        end_donate = end_donate_;

        _blockn = block.number;
	_balance = address(this).balance;
	_tx1 = Tx.I;
	_tx2 = Tx.I;	
    }


    function _delay(uint n) public {
	_blockn = _blockn + n;
    }
    
    function donate() public payable {
        require (block.number <= end_donate);
        require (_blockn <= end_donate);
        donors[msg.sender] += msg.value;
	_balance += msg.value;
	_tx1 = _tx2;
	_tx2 = Tx.D;	
    }

    function withdraw() public {
        require (block.number > end_donate);
        require (_blockn > end_donate);	
        require (_balance >= goal);
	_balance = 0;	
        (bool succ,) = receiver.call{value: address(this).balance}("");
        require(succ);

	_tx1 = _tx2;
	_tx2 = Tx.W;	
    }
    
    function reclaim() public {	
        require (block.number > end_donate);
        require (_blockn > end_donate);
	
        require (_balance < goal);
        require (donors[msg.sender] > 0);
        uint amount = donors[msg.sender];
        donors[msg.sender] = 0;
	_balance -= amount;
	
        (bool succ,) = msg.sender.call{value: amount}("");
        require(succ);

	_tx1 = _tx2;
	_tx2 = Tx.R;	
    }

    // q0 --D-> q0
    // q0 --W-> qW
    // q0 --R-> qR
    // qR --R-> qR
    function invariant() public view {
	assert(_tx2!=Tx.D || _tx1==Tx.D || _tx1==Tx.I);
	assert(_tx2!=Tx.W || _tx1==Tx.D || _tx1==Tx.I);
	assert(_tx2!=Tx.R || _tx1==Tx.D || _tx1==Tx.R);		
   }    
}
