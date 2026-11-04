# November DSA — Day 3

**Topic:** Recursion, Mathematical Division, Bit Manipulation, Reverse Greedy and Euclidean Algorithm  
**Problems covered:** 1 primary + 4 variants  

## Complexity Summary

| # | Problem | Brute-force / baseline approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Power of Two (LC 231) | Recursively divide by 2 while divisible | `O(log n)` | `O(log n)` | Check `n>0 and (n&(n-1))==0` | `O(1)`* | `O(1)`* |
| Variant 1 | Power of Three (LC 326) | Recursively divide by 3 while divisible | `O(log n)` | `O(log n)` | Iteratively divide by 3; alternatively test divisibility of `3^19` for signed 32-bit integers | `O(log n)` iterative / `O(1)`* 32-bit | `O(1)` |
| Variant 2 | Power of Four (LC 342) | Recursively divide by 4 while divisible | `O(log n)` | `O(log n)` | Check positive power of 2 and `n%3==1` | `O(1)`* | `O(1)`* |
| Variant 3 | Reaching Points (LC 780) | Recursively explore `(x+y,y)` and `(x,x+y)` | `O(2^M)` loose upper bound | `O(M)` upper bound | Work backward with modulo and fixed-coordinate divisibility tests | `O(log M)`* | `O(1)`* |
| Variant 4 | Number of 1 Bits (LC 191) | Examine each binary digit using `%2` and `//2` | `O(b)` | `O(1)` | Brian Kernighan's `n=n&(n-1)` clears one set bit per iteration | `O(k)` | `O(1)` |


## Primary — Power of Two (LC 231)

**Problem:** Return `True` if `n=2^k` for some nonnegative integer `k`; otherwise `False`. `1` is valid because `2^0=1`.

- **Brute / baseline (recursive halving):** If `n==1`, return `True`. Reject `n<=0` or odd `n>1`; otherwise recursively call with `n//2`. **Time:** `O(log n)`. **Space:** `O(log n)` recursion stack.
- **Optimized (bitwise):** A positive power of two has exactly one set bit. The operation `n&(n-1)` clears its lowest set bit, so the result must be zero. Check `n>0 and (n&(n-1))==0`. **Time:** `O(1)`*. **Space:** `O(1)`*.
- **Pattern recognition:** A question about powers of two, binary representation, or exactly one set bit often suggests `n&(n-1)`.

## Variant 1 — Power of Three

**Problem:** Return `True` if `n=3^k` for some nonnegative integer `k`; otherwise `False`.

- **Brute / baseline (recursive division):** Return `True` for `n==1`. Reject `n<=0` or `n%3!=0`; otherwise recurse on `n//3`. **Time:** `O(log n)`. **Space:** `O(log n)` recursion stack.
- **Optimized 1 (iterative division):** While `n` is positive and divisible by 3, repeatedly perform `n//=3`; return whether the final value is 1. **Time:** `O(log n)`. **Space:** `O(1)`.
- **Optimized 2 (signed 32-bit mathematical check):** `3^19=1162261467` is the largest power of 3 that fits in a signed 32-bit integer. Check `n>0 and 1162261467%n==0`. Every positive divisor of `3^19` is a power of 3. **Time:** `O(1)`*. **Space:** `O(1)`*.
- **Pattern recognition:** Check whether a number can be reduced to 1 by exact division by a fixed base. Use the constant-divisor trick only when the input range is explicitly bounded.

## Variant 2 — Power of Four

**Problem:** Return `True` if `n=4^k` for some nonnegative integer `k`; otherwise `False`.

- **Brute / baseline (recursive division):** Return `True` if `n==1`. Reject `n<=0` or `n%4!=0`; otherwise recursively call with `n//4`. **Time:** `O(log n)`. **Space:** `O(log n)` recursion stack.
- **Optimized 1 (iterative division):** Repeatedly divide a positive `n` by 4 while divisible; return whether it becomes 1. **Time:** `O(log n)`. **Space:** `O(1)`.
- **Optimized 2 (bitwise + modulo):** First require a positive power of two using `n&(n-1)==0`; then check `n%3==1`. Powers of four have even exponents of 2, unlike 2, 8, 32, etc. **Time:** `O(1)`*. **Space:** `O(1)`*.
- **Pattern recognition:** If a problem asks for powers of four, start with the power-of-two bitwise test and add a condition that distinguishes even from odd powers of 2.

## Variant 3 — Reaching Points

**Problem:** Starting from `(sx,sy)`, determine whether repeated moves `(x+y,y)` or `(x,x+y)` can reach `(tx,ty)`; all coordinates are positive.

- **Brute force (forward recursion):** From `(x,y)`, recursively explore `(x+y,y)` and `(x,x+y)`. Return `True` on matching the target; prune a branch if `x>tx` or `y>ty`. This can branch exponentially. **Time:** `O(2^M)` loose upper bound. **Space:** `O(M)` upper bound for recursion depth, where `M=max(tx,ty)`.
- **Optimized (reverse greedy + modulo):** Start from `(tx,ty)`, not `(sx,sy)`. With positive coordinates, the larger target coordinate is the one that was most recently increased. Reduce it with `tx%=ty` or `ty%=tx` to skip repeated subtractions. If `ty==sy`, test `(tx-sx)%ty==0`; if `tx==sx`, test `(ty-sy)%tx==0`. Reject values falling below the starting coordinates. **Time:** `O(log M)`* using Euclidean-style reductions. **Space:** `O(1)`*.
- **Pattern recognition:** When forward state transformations branch, but the reverse transformation is forced, work backward. Replace repeated subtraction with modulo.

## Variant 4 — Number of 1 Bits

**Problem:** Return the Hamming weight, or number of set (`1`) bits, of a 32-bit integer's binary representation.

- **Brute / baseline (bit-by-bit checking):** For nonnegative `n`, check `n%2`. If it equals 1, increment `count`; remove the last bit with `n//=2` until `n==0`. **Time:** `O(b)`. **Space:** `O(1)`.
- **Optimized (Brian Kernighan's algorithm):** Repeatedly use `n=n&(n-1)`. Each operation removes **one** rightmost set bit, so increment the counter once per operation. **Time:** `O(k)` where `k` is the set-bit count. **Space:** `O(1)`.
- **Pattern recognition:** Counting set bits or Hamming weight suggests `n&(n-1)`, especially when the input has relatively few set bits.

## Key Differences to Remember

- **Power of Two:** A positive integer is a power of two precisely when it contains one set bit; check `n&(n-1)==0`.
- **Power of Three:** Exact repeated division by 3 is the general approach; the `3^19` divisibility shortcut relies on a signed 32-bit bound.
- **Power of Four:** First identify powers of two, then distinguish the even exponents of 2 with `n%3==1`.
- **Reaching Points:** Forward recursion branches; reverse subtraction is forced by the larger coordinate. Modulo compresses repeated subtractions.
- **Number of 1 Bits:** Checking every bit takes `O(b)` steps; Kernighan's method takes only `O(k)` steps for `k` set bits.
