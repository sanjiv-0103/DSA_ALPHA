
# November DSA — Day 6

**Problems covered:** 1 primary + 2 variants  

## Complexity Summary

| # | Problem | Brute-force approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Pascal's Triangle (LC 118) | Recursively calculate each element from two values above | `O(2^n)` upper bound | `O(n²)` including output | Bottom-up DP by constructing rows from the previous row | `O(n²)` | `O(n²)` including output |
| Variant 1 | Pascal's Triangle II (LC 119) | Recursively calculate elements of the requested row | `O(2^n)` upper bound | `O(n)` | Iterative row construction using previous and current rows | `O(n²)` | `O(n)` |
| Variant 2 | Sum of Pascal Row | Construct the requested row and sum all its elements | `O(n²)` | `O(n)` | Repeated doubling using the `2^n` row-sum property | `O(n)` | `O(1)`* |


---

## Primary — Pascal's Triangle (LC 118)

**Problem:** Given an integer `numRows`, return the first `numRows` rows of Pascal's Triangle.

**Example:**

Input: `numRows=5`

Output:
`[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`

**Recurrence:** `P(row,col)=P(row-1,col-1)+P(row-1,col)`.

**Base cases:** `P(row,0)=1` and `P(row,row)=1`.

### Approach 1 — Brute-force Recursion

- Create a recursive function to calculate an individual element.
- Return `1` for the first and last positions of each row.
- For a middle element, recursively add its upper-left and upper-right values.
- Construct every row by calculating its elements recursively.
- Repeated subproblems make this approach inefficient.
- **Time:** `O(2^n)` upper bound.
- **Space:** `O(n²)` including output and recursion stack.

### Approach 2 — Optimized Bottom-Up DP

- Initialize an empty triangle.
- Create each new row containing `row+1` elements initialized to `1`.
- Calculate middle elements using adjacent values from the previous row.
- Append the completed row to the triangle.
- Each element is calculated only once.
- **Time:** `O(n²)`.
- **Space:** `O(n²)` including output.
  
---