// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.8.0) (finance/PaymentSplitter.sol)

pragma solidity ^0.8.0;

contract PaymentSplitter {

    uint256 totalShares;
    uint256 totalReleased;

    mapping(address => uint256) private shares;
    mapping(address => uint256) private released;
    address[] private payees;

    constructor(address[] memory payees_, uint256[] memory shares_) payable {
        require(payees_.length == shares_.length, "PaymentSplitter: payees and shares length mismatch");
        require(payees_.length > 0, "PaymentSplitter: no payees");

        for (uint256 i = 0; i < payees.length; i++) {
            addPayee(payees_[i], shares_[i]);
        }
    }

    receive() external payable virtual { }

    function getTotalgetShares() public view returns (uint256) {
        return totalShares;
    }

    function getTotalReleased() public view returns (uint256) {
        return totalReleased;
    }

    function getShares(address account) public view returns (uint256) {
        return shares[account];
    }

    function getReleased(address account) public view returns (uint256) {
        return released[account];
    }

    function getPayee(uint256 index) public view returns (address) {
        return payees[index];
    }

    function releasable(address account) public view returns (uint256) {
        uint256 totalReceived = address(this).balance + getTotalReleased();
        return pendingPayment(account, totalReceived, getReleased(account));
    }

    function release(address payable account) public virtual {
        require(shares[account] > 0, "PaymentSplitter: account has no shares");

        uint256 payment = releasable(account);

        require(payment != 0, "PaymentSplitter: account is not due payment");

        // totalReleased is the sum of all values in released.
        // If "totalReleased += payment" does not overflow, then "released[account] += payment" cannot overflow.
        totalReleased += payment;
        unchecked {
            released[account] += payment;
        }

        (bool success,) = account.call{value: payment}("");
        require(success);
    }

    function pendingPayment(
        address account,
        uint256 totalReceived,
        uint256 alreadyReleased
    ) private view returns (uint256) {
        return (totalReceived * shares[account]) / totalShares - alreadyReleased;
    }

    function addPayee(address account, uint256 shares_) private {
        require(account != address(0), "PaymentSplitter: account is the zero address");
        require(shares_ > 0, "PaymentSplitter: shares are 0");
        require(shares[account] == 0, "PaymentSplitter: account already has shares");

        payees.push(account);
        shares[account] = shares_;
        totalShares = totalShares + shares_;
    }

}
