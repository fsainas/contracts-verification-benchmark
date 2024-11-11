pragma solidity ^0.8.25;

import "./ExternalPayable.sol";

contract PayableInterface is I  {
	
	function f() external payable {
        revert("Too much ether");
    }
}