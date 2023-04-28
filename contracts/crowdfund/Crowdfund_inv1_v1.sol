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

    mapping(uint => uint) blockn;

    uint prev_t_id;
    uint t_id;
    
    constructor (address payable receiver_, uint end_donate_) {
        receiver = receiver_;
        end_donate = end_donate_;

	t_id = 0;
        blockn[t_id] = block.number;
	
	_tx1 = Tx.I;
	_tx2 = Tx.I;	
    }

    modifier new_t() {
        prev_t_id = t_id;
        t_id += 1;
        uint rand = uint(keccak256(abi.encode(block.number))) % 2;
        blockn[t_id] = blockn[prev_t_id] + rand;         // could be the next block or the current one
        _;
    }
    
    function donate() new_t public payable {	
        require (block.number <= end_donate);
        donors[msg.sender] += msg.value;

	_tx1 = _tx2;
	_tx2 = Tx.D;	
    }

    function withdraw() new_t public {
        require (block.number > end_donate);
        require (address(this).balance >= goal);
        (bool succ,) = receiver.call{value: address(this).balance}("");
        require(succ);

	_tx1 = _tx2;
	_tx2 = Tx.W;	
    }
    
    function reclaim() new_t public {	
        require (block.number > end_donate);
        require (address(this).balance < goal);
        require (donors[msg.sender] > 0);
        uint amount = donors[msg.sender];
        donors[msg.sender] = 0;
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
        assert(blockn[t_id] >= blockn[prev_t_id]);	
	// assert(_tx2!=Tx.D || _tx1==Tx.D || _tx1==Tx.I);
	// assert(_tx2!=Tx.W || _tx1==Tx.D);
	// assert(_tx2!=Tx.R || _tx1==Tx.D || _tx1==Tx.R);		
   }    
}
