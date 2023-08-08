### Certora

### True Negatives

When Certora claims violation of a property, it does not distinguish between having *proven* that the property is false, and not having *been able to verify* that the property always holds. As an example, consider the following contract and rule.

```solidity
contract Example {
    uint received;
    uint received_copy;

    function getReceived() public view returns (uint) { return received; }
    function getReceivedCopy() public view returns (uint) { return received_copy; }

    function send() payable public {
        received = received + msg.value;
        received_copy = received_copy + msg.value;
    }

    function foo(uint x) public view {
        require(x <= received_copy);
    }
}
```
This contract is composed of mainly two functions: a `send` function that receives ETH and stores the received amount in the `received` and `received_copy` variables; and a `foo` function, which checks that the provided `x` is at most `received_copy`.

```solidity
rule bar {
    env e;
    uint x;

    require x <= getReceived(e);

    foo@withrevert(e, x);
    assert !lastReverted;
}
```
The specification states that no call to `foo` should revert when the provided `x` is at most the `received` amount. Naturally as `received_copy` is updated together with `received`, their values are synchronized and the rule is not violated.

If we check the specification against the [contract](https://prover.certora.com/output/49230/84bb1b530f844988a4edd6cf7119fde4?anonymousKey=319ae35285547c82bde75076f832c36c97898089) and against a [variation of it](https://prover.certora.com/output/49230/268e2da5c72047e991ada1617800babe?anonymousKey=d67ef5f9ee26cc08159fd05a3332593d7c242d3d) in which the `received_copy` variable is not updated, Certora gives us the same answer: that there is a call trace that violates the property. The two call traces are equal, but in the case of the original contract, the initial state from which the trace starts (`received=8`, `received_copy=0`) is not reachable. Since Certora does not tell us when it is sure that a call trace is possible or not, we cannot label any of the violating cases as True Negative, but only as unknown.

### False Negative

False Negatives can only be handled in a best effort manner. Considering the same example as before, by modifying the specification slightly (augmenting it with an invariant) we are [able to verify](https://prover.certora.com/output/49230/5f1294ebd040423ba07acb270636bd72?anonymousKey=7554badba26aecd510e1d1122aff67ef573ea511) the property that was previously flagged as violated.

```solidity
invariant R_R1_eq(env e) 
    getReceived(e) == getReceived1(e);

rule bar {
    env e;
    uint amount;

    requireInvariant R_R1_eq(e);
    require amount <= getReceived(e);

    foo@withrevert(e, amount);
    assert !lastReverted;
}
``` 

We must therefore be careful on what we flag as False Negative, as the property might not be too complex to be verified, but the specification might just not be complete enough.
