pragma solidity ^0.8.25;

import "./MutexUnsafe.sol";

contract Attack {
	fallback() external {
		MutexUnsafe mutex_unsafe = MutexUnsafe(msg.sender);
		mutex_unsafe.set(5);
	}
}