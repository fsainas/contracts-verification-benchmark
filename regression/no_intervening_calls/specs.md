The `NoInterveningCalls` contract manages a boolean state variable `b` with two functions:

- `f()`: A no-op function that performs no state changes.
- `g()`: A function that modifies the state by setting `b` to `false`.

When `f()` is called two times in a row and `g()` is not called, the value of `b` should not change.