# Crowdfund

## Specification

Crowdfund is contract a for conducting crowdfunding campaigns. It allows users
to donate ether to a specified receiver within a certain timeframe. The
contract ensures that the crowdfunding campaign is successful if the total
donated amount reaches a predefined goal. Otherwise, donors can reclaim their
donations after the donation period has ended.

## Versions

- **v1**: conformant to specification
- **v2**: virtual block number with [BlockNumberSMT](../../smtCheckerNotes/block_number/)
- **v3**: virtual block number with `delay()`

## Properties

- **p1**:
    - if the current transaction is a donation, the phase is 'donate'
    - if the current transaction is a withdraw, the phase is 'withdraw'
    - if the current transaction is a reclaim, the phase is either 'withdraw or reclaim' or 'withdraw'

## Experiments

|        | p1                 |
| ------ | ------------------ |
| **v1** | :x:                |
| **v2** | :question:         |
| **v3** | :heavy_check_mark: |
