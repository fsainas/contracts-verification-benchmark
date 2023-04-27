// SPDX-License-Identifier: GPL-3.0-only
pragma solidity >= 0.8.2;

contract BlockNumberSMT {
    mapping(uint => uint) private _block_number;
    uint private _transaction_id;
    uint private _prev_transaction_id;

    modifier new_t() {
        _new_transaction();
        _;
    }

    function block_number() internal view returns (uint) {
        return _block_number[_transaction_id];
    }

    function _new_transaction() private {
        _prev_transaction_id = _transaction_id;
        _transaction_id += 1;
        uint rand = uint(block.timestamp) % 2;
        _block_number[_transaction_id] = _block_number[_prev_transaction_id] + rand;         // could be the next block or the current one
    }
}
