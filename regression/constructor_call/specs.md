The `ConstructorCall` contract is designed to initialize and manage a list of values provided during contract deployment. It performs basic aggregation and storage operations on these values, ensuring certain constraints are met. Below are the key specifications:

## **Initialization via Constructor**
- The contract requires an array of unsigned integers (`uint256[]`) as input during deployment.
- The length of the input array must match a predefined constant (`LENGHT`), which is set to **10**.
- Each value in the array is validated to ensure it is **greater than zero** before being processed.


## **Sum Calculation**
- The contract maintains a private variable `sum` that aggregates the values provided during deployment.
- The `doSum` function is used to:
  - Add each value to the `sum`.
  - Store the value in the `values` array.


## **Storage of Values**
- The contract stores all validated values in a private array `values`.
- These values can be accessed indirectly through the `getSumOfValues` function.


## **Getter Function for Aggregation**
- The `getSumOfValues` function:
  - Calculates and returns the sum of all values stored in the `values` array.
  - Provides visibility into the aggregated data for verification purposes.
