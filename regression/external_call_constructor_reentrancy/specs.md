We have the contract `ExternalCallConstructorReentrancy` and the interface `D`.
### D interface
`D` is an interface and it defines an external function `ext` which takes the an `ExternalCallConstructorReentrancy` contract as argument and returns a `uint`.
```
interface D {
	function ext(ExternalCallConstructorReentrancy c) external returns (uint);
}
```

### ExternalCallConstructorReentrancy contract
`ExternalCallConstructorReentrancy` has the function `s` and the constructor.

The function `s` takes a uint value and assigns it to the `x` variable.
```
function s(uint _x) public {
	x = _x;
}
```
The constructor takes a `D` interface and calls the `ext` function of the interface with the current contract as argument.
```
constructor(D d) {
    uint a = d.ext(this);
}
```