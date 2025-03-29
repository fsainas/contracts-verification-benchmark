// SPDX-License-Identifier: MIT
pragma solidity >= 0.8.2;

import "./IERC20.sol";

/**
 * @dev Implementation of the {IERC20} interface.
 *
 */
contract ERC20 is IERC20 {
    mapping(address => uint256) private _balances;
    uint256 private _totalSupply;

    constructor(uint256 amount) {
        _totalSupply += amount;
	    _balances[msg.sender] += amount;
    }

    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * Requirements:
     * - `to` cannot be the zero address.
     * - the caller must have a balance of at least `amount`.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    function allowance(address owner, address spender) public view returns (uint256) {
        require (owner != address(0));
	require (spender != address(0));
	return _balances[owner];
    }

    /**
     * NOTE: If `amount` is the maximum `uint256`, the allowance is not updated on
     * `transferFrom`. This is semantically equivalent to an infinite approval.
     *
     * Requirements:
     * - `spender` cannot be the zero address.
     */
    function approve(address spender, uint256 amount) public view returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev See {IERC20-transferFrom}.
     *
     *
     * NOTE: Does not update the allowance if the current allowance
     * is the maximum `uint256`.
     *
     * Requirements:
     *
     * - `from` and `to` cannot be the zero address.
     * - `from` must have a balance of at least `amount`.
     * - the caller must have allowance for ``from``'s tokens of at least
     * `amount`.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        _spendAllowance(from, msg.sender, amount);
        _transfer(from, to, amount);
        return true;
    }

    function _transfer(address from, address to, uint256 amount) internal {
        require (from != address(0));
	require (to != address(0));

	uint256 fromBalance = _balances[from];
	require (fromBalance >= amount);
	// unchecked {
	// Overflow not possible: amount <= fromBalance <= totalSupply.
	_balances[from] = fromBalance - amount;
	// Overflow not possible: balance + amount is at most totalSupply, which we know fits into a uint256.
	_balances[to] += amount;
	// }
    }

    /**
     * @dev Sets `amount` as the allowance of `spender` over the `owner` s tokens.
     *
     * This internal function is equivalent to `approve`, and can be used to
     * e.g. set automatic allowances for certain subsystems, etc.
     *
     * Requirements:
     *
     * - `owner` cannot be the zero address.
     * - `spender` cannot be the zero address.
     */
    function _approve(address owner, address spender, uint256 amount) internal pure {
        require (owner != address(0));
	require (spender != address(0));
	require (amount >= 0);
    }

    /**
     * @dev Updates `owner` s allowance for `spender` based on spent `amount`.
     *
     * Does not update the allowance amount in case of infinite allowance.
     * Revert if not enough allowance is available.
     *
     */
    function _spendAllowance(address owner, address spender, uint256 amount) internal view {
        uint256 currentAllowance = allowance(owner, spender);
        require (currentAllowance >= amount);
	_approve(owner, spender, currentAllowance);
    }
}
