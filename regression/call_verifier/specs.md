The contract has only the function `f` that performs an external call:
```
function f(address a) public {
    (bool s, bytes memory data) = a.call("");
}
```
The properties `call-failure` and `call-success` should both fail since we cannot know if the call will fail or not.

The property `ex-call-is-made` check if an external call appened.