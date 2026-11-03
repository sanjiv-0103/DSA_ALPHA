# Day 27 - Implement Queue using Stacks

| Problem | Approach | Main Operation | Space |
|---|---|---|---|
| Implement Queue using Stacks | Brute force - transfer between two stacks for every pop/peek | O(n) | O(n) |
| Implement Queue using Stacks | Optimized - input stack + output stack | Amortized O(1) | O(n) |
| Moving Average from Data Stream | Brute force - calculate complete sum for each value | O(k) | O(k) |
| Moving Average from Data Stream | Optimized - maintain running total | O(1) sum calculation | O(k) |

## Primary - Brute Force Logic
- Use two stacks
- Push new values into the first stack
- For pop or peek, move all values to the second stack
- The oldest value becomes the top value
- Move the remaining values back again.

## Primary - Optimized Logic
- Use an input stack and output stack
- Push new values into the input stack
- Transfer values only when the output stack is empty
- The top of the output stack is the front of the queue
- This avoids repeated transfers

## Variant - Brute Force Logic
- Store the latest values
- Remove the oldest value when the size limit is exceeded
- Recalculate the total for every new value

## Variant - Optimized Logic
- Keep a running total
- Add the new value to the total
- Subtract the oldest value when it is removed
- Calculate average using the current total
