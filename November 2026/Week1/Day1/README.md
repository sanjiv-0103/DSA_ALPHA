# November DSA — Day 1

**Topic:** Recursion, Memoization, Dynamic Programming and Mathematical Patterns  
**Problems covered:** 1 primary + 4 variants  

## Complexity Summary

| # | Problem | Brute-force approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Fibonacci Number | Recursive branching using `fib(n-1)+fib(n-2)` | `O(2^n)` upper bound | `O(n)` | Top-down recursion with dictionary memoization | `O(n)` | `O(n)` |
| Variant 1 | N-th Tribonacci Number | Recursive branching using previous three terms | `O(3^n)` upper bound | `O(n)` | Top-down recursion with dictionary memoization | `O(n)` | `O(n)` |
| Variant 2 | Climbing Stairs | Recursively count paths via one-step and two-step moves | `O(2^n)` upper bound | `O(n)` | Iterative DP with two previous results | `O(n)` | `O(1)` |
| Variant 3 | Min Cost Climbing Stairs | Recursively evaluate both next steps and take the minimum | `O(2^n)` upper bound | `O(n)` | Top-down recursion with dictionary memoization | `O(n)` | `O(n)` |
| Variant 4 | Factorial Trailing Zeroes | Compute `n!`, then repeatedly strip terminal zero digits | `O(n)`* | `O(1)`* | Repeatedly divide `n` by 5 and add the quotients | `O(log n)` | `O(1)` |

## Primary — Fibonacci Number (LC 509)

**Problem:** Return the `n`th Fibonacci number, with `F(0)=0`, `F(1)=1`.

**Recurrence:** `F(n)=F(n-1)+F(n-2)`.

- **Brute force:** Use recursion and stop at `n<=1`. Recompute the same Fibonacci values on different branches. **Time:** `O(2^n)` upper bound. **Space:** `O(n)` recursion stack.
- **Optimized (memoization):** Maintain a dictionary `memo`. Before making recursive calls, return the cached answer when present; otherwise compute, save and return it. **Time:** `O(n)`. **Space:** `O(n)` for cache + stack.
- **Pattern recognition:** A sequence defined by previous terms with overlapping recursive subproblems.

## Key Differences to Remember

- **Fibonacci / Tribonacci:** Sum previous terms; cache repeated subproblems.
- **Climbing Stairs:** Count distinct ways; **add** possible counts.
- **Min Cost Climbing Stairs:** Find cheapest path; take **minimum** of possible next costs.
- **Factorial Trailing Zeroes:** Use prime-factor counting; avoid constructing the factorial.

## Viva Quick Revision

1. **Why memoization?** It stores repeated subproblem results to reduce exponential recursion to linear work.
2. **Why does memoized recursion use `O(n)` space?** Both its dictionary and maximum call-stack depth are linear.
3. **Why is iterative Climbing Stairs `O(1)` space?** Only the previous two totals are retained.
4. **Why `min()` for Min Cost Climbing Stairs?** We want one cheapest path, not the total number of paths.
5. **Why count fives for factorial trailing zeroes?** Each zero requires a `2×5` pair, and factors of 2 are more numerous.
