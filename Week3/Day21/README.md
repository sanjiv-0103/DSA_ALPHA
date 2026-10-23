# Day 21 - Range Sum Query Immutable

| Problem | Approach | Build Time | Query Time | Space |
|---|---|---|---|---|
| Range Sum Query | Brute force - add values from left to right for every query | O(1) | O(n) | O(1) |
| Range Sum Query | Optimized - build prefix sum once and use subtraction | O(n) | O(1) | O(n) |

## Brute Force Logic
- Store the original array.
- For every query, loop from `left` to `right`.
- Add all values and return the total.
- Simple but slow when there are many queries.

## Optimized Logic
- Build a prefix sum array once.
- Each position stores the running sum.
- Range sum is calculated using:

`prefix[right+1]-prefix[left]`

- This makes every query O(1).