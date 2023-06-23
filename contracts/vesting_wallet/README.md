# Vesting Wallet

## Specification

The VestingWallet contract handles the maturation (vesting) of native
cryptocurrency for a given beneficiary.
The constructor specifies the address of the `beneficiary`,
the first block height (`start`) where the beneficiary can withdraw funds,
and the overall `duration` of the vesting scheme.
Once the scheme is expired, the beneficiary can withdraw
all the funds from the contract.
At any moment between the start and the expiration of the vesting scheme,
the beneficiary can withdraw an amount of ETH proportional to the time
passed since the start of the scheme.
The contract can receive ETH at any time through external transactions:
these funds will follow the vesting schedule as if they were
deposited from the beginning.


## Properties

- **p1**: the amount of releasable ETH is always less than or equal to the contract balance.
- **p2**: if the vesting scheme has expired, then the whole contract balance is releasable.
- **p3**: if the vesting scheme has not started yet, then no balance is releasable.
- **p4**: before the expiration of the scheme, the releasable amount is strictly increasing
  whenever the contract balance is constant.


## Versions

- **v1**: from [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/finance/VestingWallet.sol);


## Experiments

### SolCMC

|      | **p1** | **p2** | **p3** | **p4** |
| ---- | ------ | ------ | ------ | -------|
|**v1**| FP     | FP     | TP     | ?      |
