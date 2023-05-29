// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.8.0) (finance/VestingWallet.sol)
pragma solidity ^0.8.0;

contract VestingWallet {

    uint256 private released;
    address private immutable beneficiary;
    uint64 private immutable start;
    uint64 private immutable duration;

    // ghost variables
    uint releasable1;
    uint releasable2;
    bool isReleasable1Recorded;
    uint timestamp1;
    uint balance1;

    constructor(address beneficiaryAddress, uint64 startTimestamp, uint64 durationSeconds) payable {
        require(beneficiaryAddress != address(0), "VestingWallet: beneficiary is zero address");
        beneficiary = beneficiaryAddress;
        start = startTimestamp;
        duration = durationSeconds;
    }

    receive() external payable virtual {}

    function releasable() public virtual returns (uint256) {
        if (!isReleasable1Recorded) {
            releasable1 = vestedAmount(uint64(block.timestamp)) - released;
            timestamp1 = block.timestamp;
            isReleasable1Recorded = true;
            balance1 = address(this).balance;
        } else {
            require(timestamp1 != block.timestamp);
            require(balance1 == address(this).balance);
            releasable2 = vestedAmount(uint64(block.timestamp)) - released;
            assert(releasable1 < releasable2);
        }
        return vestedAmount(uint64(block.timestamp)) - released;
    }

    function release() public virtual {
        uint256 amount = releasable();
        released += amount;

        (bool success, ) = beneficiary.call{value: amount}("");
        require(success);
    }

    function vestedAmount(uint64 timestamp) public view virtual returns (uint256) {
        return vestingSchedule(address(this).balance + released, timestamp);
    }

    function vestingSchedule(uint256 totalAllocation, uint64 timestamp) internal view virtual returns (uint256) {
        if (timestamp < start) {
            return 0;
        } else if (timestamp > start + duration) {
            return totalAllocation;
        } else {
            return (totalAllocation * (timestamp - start)) / duration;
        }
    }

}
