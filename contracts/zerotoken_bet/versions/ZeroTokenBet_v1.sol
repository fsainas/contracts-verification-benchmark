/// @custom:version compliant with the specification.
// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract ZeroTokenBet {

    address public a;
    address public b;
    address public oracle;
    uint timeout_block;
    int balance;   // contract balance
    int balance_a; // balance of a
    int balance_b; // balance of b
	
    constructor(address p, address o, uint t) payable {
        a = msg.sender;
        b = p;
        oracle = o;
        timeout_block = t;

        balance_a = 0;
        balance_b = 1;
        balance = 1;	
    }
    
    function deposit() public {
        require (block.number <= timeout_block);
        require (msg.sender==b);
        require (balance>=1); // needed for single run 
        require (balance_b>=1);
        balance_b = balance_b - 1;
        balance = balance + 1;
    }

    function win(address dst) public {
        require (block.number <= timeout_block);
        require (msg.sender==oracle);
        require (dst==a || dst==b);
        require (balance>=2);
        if (dst==a) { balance_a += balance; balance = 0; } 
        else if (dst==b) { balance_b += balance; balance = 0; }
    }

    function timeout() public {
        require (block.number > timeout_block);

	// transfers 1 token to a
        require (balance>=1);
        balance_a += 1;
        balance -= 1;

	// transfers 1 token to b
        require (balance>=1);	
        balance_b += 1;
        balance -= 1;
   }    
}
