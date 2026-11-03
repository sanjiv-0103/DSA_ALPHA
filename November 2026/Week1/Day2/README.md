# November DSA — Day 2

**Topic:** Recursion, Bottom-Up Dynamic Programming, Space Optimization and Mathematical Patterns  
**Problems covered:** 1 primary (2 DP approaches) + 3 variants  

## Complexity Summary

| # | Problem | Brute-force approach | Brute time | Brute space | Optimized approach  | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Climbing Stairs  | Recursively add ways from `n-1` and `n-2` | `O(2^n)` upper bound | `O(n)` | Bottom-up DP list (`climbstairs_dplist.py`); further optimized rolling two variables (`climbstairs_optimized_dp.py`) | `O(n)` for both | `O(n)` DP list; `O(1)` rolling variables |
| Variant 1 | Count Ways to Reach N-th Stair (1, 2 or 3 steps) | Recursively add ways from `n-1`, `n-2`, `n-3` | `O(3^n)` upper bound | `O(n)` | Iterative rolling three variables (`countways_optimized.py`) | `O(n)` | `O(1)` |
| Variant 2 | Reach a Number  | Explore left/right directions recursively for increasing move counts (conceptual comparison; not a separate file) | `O(2^k)` | `O(k)` | Greedy triangular sum and parity check (`reachnum.py`) | `O(sqrt(abs(target)+1))` | `O(1)` |
| Variant 3 | Decode Ways | Recursively try valid one-digit and two-digit decodings (`decode.py`) | `O(2^n)` upper bound | `O(n)` | Bottom-up DP list (`decode_optimized.py`) | `O(n)` | `O(n)` |

Here, `n` means the number of stairs or digits (depending on the problem); `k` is the minimum number of moves in Reach a Number. Complexities use the usual constant-time arithmetic model.

## Primary — Climbing Stairs 

**Problem:** Count the distinct ways to climb `n` stairs when each move is 1 or 2 steps.  
**Recurrence:** `ways(n)=ways(n-1)+ways(n-2)` with `ways(1)=1`, `ways(2)=2`.

- **Brute force (recursion):** Recursively calculate both previous states and add their answers, recalculating overlapping subproblems. **Time:** `O(2^n)` upper bound. **Space:** `O(n)` recursion stack.
- **Optimized — DP list (`climbstairs_dplist.py`):** Create `dp=[0]*(n+1)`, set `dp[1]=1`, `dp[2]=2`, and fill `dp[i]=dp[i-1]+dp[i-2]` for `i=3...n`. **Time:** `O(n)`. **Space:** `O(n)` for the list.
- **Further optimized — two variables (`climbstairs_optimized_dp.py`):** Keep `prev1=2` and `prev2=1`; compute `curr=prev1+prev2`, then shift the variables. **Time:** `O(n)`. **Space:** `O(1)` auxiliary.
- **Pattern recognition:** Counting paths when every move has two fixed choices; answer depends only on the two preceding counts.

## Variant 1 — Count Ways to Reach the N-th Stair (3 Steps)

**Problem:** Count distinct ways to climb `n` stairs when moves of 1, 2 or 3 steps are allowed.  
**Recurrence:** `ways(n)=ways(n-1)+ways(n-2)+ways(n-3)` with `ways(0)=1`, `ways(n<0)=0`.

- **Brute force (`countways.py`):** Use recursive branching for all three jump sizes. Stop with `1` at exactly zero remaining steps and `0` below zero. **Time:** `O(3^n)` upper bound. **Space:** `O(n)` recursion stack.
- **Optimized (`countways_optimized.py`):** Use rolling variables `prev1`, `prev2`, `prev3`, initialized to `2`, `1`, `1` (ways for 2, 1, 0 steps); calculate each next count from their sum and shift the values. **Time:** `O(n)`. **Space:** `O(1)` auxiliary.
- **Pattern recognition:** Counting paths with three fixed jump sizes; Tribonacci-like recurrence with stair-counting base cases.

## Variant 2 — Reach a Number 

**Problem:** Starting at position 0, move exactly 1 unit on move 1, 2 units on move 2, etc., choosing left or right each time. Return the minimum moves needed to reach `target`.

- **Brute-force idea (not separately implemented):** Try both directions recursively for each move count until a path reaches the target. For a search up to `k` moves, **time:** `O(2^k)`; **space:** `O(k)` recursion stack.
- **Optimized (`reachnum.py`):** Convert the target to its absolute value. Increment `moves` and add each jump to `total` until `total>=target` **and** `(total-target)%2==0`. Reversing a jump changes the total by an even amount, so the parity check determines reachability. **Time:** `O(sqrt(abs(target)+1))`. **Space:** `O(1)` auxiliary.
- **Pattern recognition:** Increasing jump distances, triangular numbers (`1+2+...+k`) and even/odd parity; no DP table is needed.

## Variant 3 — Decode Ways

**Problem:** Count valid ways to decode a numeric string using `1=A` through `26=Z`. A standalone `0` is invalid.

- **Brute force (`decode.py`):** From each index, recurse by taking a nonzero single digit; also try a two-digit code if it lies in `10...26`. Reaching the end gives one valid decoding. **Time:** `O(2^n)` upper bound. **Space:** `O(n)` recursion stack.
- **Optimized (`decode_optimized.py`):** Build a DP list where `dp[i]` counts valid decodings of the first `i` characters. Set `dp[0]=1`; add `dp[i-1]` for a valid last single digit and `dp[i-2]` for a valid last pair. **Time:** `O(n)`. **Space:** `O(n)` for the DP list.
- **Pattern recognition:** Counting valid ways to partition a string into one- or two-character groups, with conditions on each group.

## Key Differences to Remember

- **Climbing Stairs:** Add two previous counts; DP list uses `O(n)` space, rolling variables use `O(1)`.
- **Count Ways (3 Steps):** Add three previous counts; the implemented optimized solution keeps three rolling values.
- **Reach a Number:** Find a minimum move count using triangular sums and parity rather than DP.
- **Decode Ways:** Add one-digit and two-digit counts **only when the selected code is valid**; `0` cannot stand alone.
