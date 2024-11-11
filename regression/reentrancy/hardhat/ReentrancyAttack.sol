pragma solidity ^0.8.25;

import "./Reentrancy.sol";

contract ReentrancyAttack {
    fallback() external{
        Reentrancy reentrancy = Reentrancy(msg.sender);
        reentrancy.s(5);
    }
}