// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.8.0) (finance/VestingWallet.sol)
pragma solidity >= 0.8.2;

contract VestingWallet {

    uint256 private released;
    address private immutable beneficiary;
    uint64 private immutable start;
    uint64 private immutable duration;

    constructor(address beneficiaryAddress, uint64 startTimestamp, uint64 durationSeconds) payable {
        require(beneficiaryAddress != address(0), "VestingWallet: beneficiary is zero address");
        beneficiary = beneficiaryAddress;
        start = startTimestamp;
        duration = durationSeconds;
    }

    receive() external payable virtual {}

    function releasable() public view virtual returns (uint256) {
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

    // p1: the amount of releasable ETH is always <= the contract balance
    function invariant() public view {
        assert(releasable() <= address(this).balance);
    }

}
