pragma solidity ^0.8.25;

import "./Payable.sol";

contract SecondPayable {
	receive() external payable {
        revert("Too much ether");
    }
}