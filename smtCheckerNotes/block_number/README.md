# Block Number
This is one way around the problem of `block.number >= prev_block.number` missing
constraint.\
Key ingredients are:
- `t_id` $\to$ current transaction id;
- `prev_t_id` $\to$ previous transaction id;
- `mapping(uint => uint) blockn` $\to$ from transaction ids to block numbers;
- `modifier new_t()` $\to$ represents a new transaction.

When a function with `new_t()` is called the state of the three previous data
structures are updated. This method could break in cases of internal calls.
