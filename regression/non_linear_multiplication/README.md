# Non Linear Mult

## Specification
The `NonLinearMult` contract is designed to perform multiplication operations using stored values initialized during deployment. It maintains constant and variable values to compute products through different mathematical relationships. Below are the key specifications:

## **Initialization via Constructor**
- The contract requires a single unsigned integer (`uint _a`) as input during deployment.
- The constructor initializes two private state variables:
  - `a` is set to the provided input value `_a`
  - `b` is set to the value of the constant `c`
- No validation constraints are applied to the input parameter.

## **Constant Definition**
- The contract defines a private constant `c` with a fixed value of **3**.
- This constant serves as a multiplier and initialization value throughout the contract's operations.
- The constant cannot be modified after contract deployment.

## **State Variable Management**
- The contract maintains two private state variables:
  - `a`: Stores the user-provided value from constructor initialization
  - `b`: Stores the constant value (always equal to `c = 3`)
- Both variables are private and can only be accessed through the contract's public functions.

## **Multiplication Functions**
- The contract provides two public view functions for retrieving multiplication results:

### **Variable-Based Multiplication (`getAB`)**
- The `getAB` function:
  - Multiplies the stored variable `a` by the stored variable `b`
  - Returns the product `a * b`
  - Since `b` is always equal to `c`, this effectively computes `a * 3`

### **Constant-Based Multiplication (`getAC`)**
- The `getAC` function:
  - Multiplies the stored variable `a` by the constant `c`
  - Returns the product `a * c`
  - This always computes `a * 3` directly using the constant

## Properties
- **ab-eq-ac**: The product of two variables, `a` and `b`, should be equal to the product of the same `a` with a constant `c`, if `b` is given the same value of `c`
- **correct-modulo-ab**: the output of ab should be always divisible by 3
- **correct-modulo-ac**: the output of ac should be always divisible by 3

## Ground truth
|        | ab-eq-ac          | correct-modulo-ab | correct-modulo-ac |
|--------|-------------------|-------------------|-------------------|
| **v1** | 1                 | 1                 | 1                 |
 

## Experiments
### SolCMC
#### Z3
|        | ab-eq-ac          | correct-modulo-ab | correct-modulo-ac |
|--------|-------------------|-------------------|-------------------|
| **v1** | UNK               | TP!               | TP!               |
 

#### ELD
|        | ab-eq-ac          | correct-modulo-ab | correct-modulo-ac |
|--------|-------------------|-------------------|-------------------|
| **v1** | TP!               | TP!               | TP!               |
 


### Certora
|        | ab-eq-ac          | correct-modulo-ab | correct-modulo-ac |
|--------|-------------------|-------------------|-------------------|
| **v1** | FN                | FN                | TP!               |
 

