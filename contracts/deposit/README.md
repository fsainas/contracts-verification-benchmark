# Deposit
This contract implements a simple deposit and withdraw mechanism. The functions
to deposit ethers can be `deposit()` or `receive()` and `fallback()`, plus the
deposit that can be done through the `constructor()`. There are always two
functions to withdraw: `withdraw(uint _amount)` and `withdraw_all()`.

## Purpose 
These tests are aimed at find out in what cases SMTChecker/SolCMC cannot prove
that the amount withdraw from the contract is always less then or equal to the
total amount deposited. We do this by using the following variables and
functions:

- `uint deposited` $\to$ total amount deposited in the contract;
- `uint sent` $\to$ total amount withdraw from the contract;
- `uint balance` $\to$ current contract balance;
- `function invariant() public view` $\to$ simple `assert(sent <= deposited)`.

## Types of Withdraw
Three types of withdrawal are tested:

- *Virtual State* $\to$ the withdraw is simulated by updating `sent` and
  `balance`. There are no external calls, transfers of ethers or possible
  failures;
- *External Calls* $\to$ `sent` and `balance` are updated before an external
  call to send ethers to the address that called the withdraw function;
- *Manual Reverting* $\to$ the failure of the transacion is simulated with an
  expression that can be equal to $0$ or $1$ assigned to the variable `succ`.
  If `succ == 0` the value of `send` and `balance` is manually reverted.

## Contract Variants
> - :heavy_check_mark: $\to$ property proved
> - :question: $\to$ SMTChecker/SolCMC does not terminate
> - :x: $\to$ SMTChecker/SolCMC could not prove the property

### Virtual Balance
These contracts do not interact with the `address(this).balance` so there is no
link between the `balance` variable and the real balance of the contract.

- **Virtual Deposits** $\to$ No real ethers can be deposited in the contract
  after deployment since no payable functions or `receive()` and `fallback()`
  are defined [^1]. The constructor accepts an `uint _amount` parameter which
  simulates an initial deposit and it is added to `balance` and to `deposited`.
  The `deposit()` function operates in the same way.
  ```
  constructor(uint _amount) {
      balance = _amount;
      deposited = _amount;
  }

  function deposit(uint _amount) public {
      balance += _amount;
      deposited += _amount;
  }
  ```
    - *Virtual State* :heavy_check_mark:
    - *External Calls* :heavy_check_mark:
    - *Manual Reverting* :heavy_check_mark:
- **Payable Constructor** $\to$ at deployment time, real ethers can be sent to
  the contract through the constructor. The amount is assigned to `balance` and
  `deposited`.
  ```
  constructor () payable {
      balance = msg.value;
      deposited = msg.value;
  }

  function deposit(uint _amount) public {
      balance += _amount;
      deposited += _amount;
  }
  ```
    - *Virtual State* :heavy_check_mark:
    - *External Calls* :heavy_check_mark:
    - *Manual Reverting* :heavy_check_mark:
- **Payable Deposit \& Constructor** $\to$ real ethers can be sent to the
  contract with the constructor and the deposit function, the amount is added
  to `balance` and `deposited`.
  ```
  constructor () payable {
      balance = msg.value;
      deposited = msg.value;
  }

  function deposit() public payable {
      balance += msg.value;
      deposited += msg.value;
  }
  ```
    - *Virtual State* :heavy_check_mark:
    - *External Calls* :heavy_check_mark:
    - *Manual Reverting* :heavy_check_mark:

### Real Contract Balance
In these variants there is a certain degree of link with the real balance of
the contract and interaction with the `address(this).balance` variable.

- **Virtual Deposits** $\to$ at deployment time, the real balance of the
  contract (`address(this).balance`) is recorded and saved into `balance` and
  `deposited`.
  ```
  constructor () {
      balance = address(this).balance;
      deposited = address(this).balance;
  }

  function deposit(uint _amount) public {
      balance += _amount;
      deposited += _amount;
  }
  ```
    - *Virtual State* :heavy_check_mark:
    - *External Calls* :heavy_check_mark:
    - *Manual Reverting* :heavy_check_mark:
    - *External Calls With an Alternative Contract Name* [^2] :question:
- **Payable Deposit** $\to$ real ethers can be deposited through `deposit()`.
  ```
  constructor () {
      balance = address(this).balance;
      deposited = address(this).balance;
  }

  function deposit() public payable {
      balance += msg.value;
      deposited += msg.value;
  }
  ```
    - *Virtual State* :heavy_check_mark:
    - *External Calls* :heavy_check_mark:
    - *Manual Reverting* :heavy_check_mark:
    - *External Calls With an Alternative Contract Name* [^2] :heavy_check_mark:
- **Receive and Fallback** $\to$ real balance in the constructor. Receive
  and fallback functions are used to deposit ethers.
  ```
  constructor () {
      balance = address(this).balance;
      deposited = address(this).balance;
  }

  receive() external payable {
      balance += msg.value;
      deposited += msg.value;
  }

  fallback() external payable {
      balance += msg.value;
      deposited += msg.value;
  }
  ```
    - *Virtual State* :heavy_check_mark:
    - *External Calls* :question: 
    - *Manual Reverting* :heavy_check_mark:

### No `balance` Variable
These contracts use only the `address(this).balance` variable and do not keep
track of a virtual balance.

- **Virtual Deposit** $\to$ the balance at deployment time is recorded in the
  `deposited` variable. No real ethers can be sent to the contract.
  ```
  constructor () {
      deposited = address(this).balance;
  }

  function deposit(uint _amount) public {
      deposited += _amount;
  }
  ```
    - *Virtual State* :x:
    - *External Calls* :question:
    - *Manual Reverting* :x:
- **Payable Deposit** $\to$ the balance at deployment time
  is recorded in the `deposited` variable. Real ethers can be deposited through
  `deposit()`.
  ```
  constructor () {
      deposited = address(this).balance;
  }

  function deposit() public payable {
      deposited += msg.value;
  }
  ```
    - *Virtual State* :x:
    - *External Calls* :question:
    - *Manual Reverting* :x:
- **Receive and Fallback** $\to$ real balance in the constructor. Receive
  and fallback functions are used to deposit ethers.
  ```
  constructor () {
      deposited = address(this).balance;
  }

  receive() external payable {
      deposited += msg.value;
  }

  fallback() external payable {
      deposited += msg.value;
  }
  ```
    - *Virtual State* :x:
    - *External Calls* :question:
    - *Manual Reverting* :x:

[^1]: [Contract without `receive()` or `fallback()`
  (docs)](https://docs.soliditylang.org/en/latest/contracts.html#receive-ether-function)

[^2]: Changed the name of the contract from `Deposit` to `Simple`, SMTChecker seems to be stuck.
