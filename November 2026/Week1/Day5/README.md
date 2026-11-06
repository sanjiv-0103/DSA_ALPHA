# November DSA — Day 5

**Topic:** Bit Manipulation, Modular Arithmetic, Binary Search, Base Conversion and Divisor Pairs  
**Problems covered:** 1 primary + 3 variants  

## Complexity Summary

| # | Problem | Brute / Baseline approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Power of Four (LC 342) | Recursively divide by 4 | `O(log n)` | `O(log n)` | Bitwise single-set-bit check + `n%3==1` | `O(1)`* | `O(1)`* |
| Variant 1 | Valid Perfect Square (LC 367) | Test successive integers by squaring | `O(√n)` | `O(1)` | Binary search over candidate roots | `O(log n)` | `O(1)` |
| Variant 2 | Base 4 Representation | Recursively convert `n//4` and concatenate `n%4` | `O(d²)`** | `O(d²)`** upper bound | Extract digits into list, reverse manually, join | `O(d)` | `O(d)` |
| Variant 3 | Check Perfect Number (LC 507) | Sum all proper divisors from 1 to `n-1` | `O(n)` | `O(1)` | Sum divisor pairs while `val*val<=n` | `O(√n)` | `O(1)` |


---

## Primary — Power of Four (LC 342)

**Problem:** Return `True` if the integer `n` is a power of four, otherwise `False`.

**Examples:** `16 → True`, `8 → False`, `1 → True`.

- **Approach 1 — Recursive division:** Return `True` for `n==1`; return `False` if `n<=0` or `n%4!=0`; otherwise check `n//4` recursively. **Time:** `O(log n)`. **Space:** `O(log n)` for the call stack.
- **Approach 2 — Iterative division:** While `n>0` and divisible by 4, divide it by 4; then test `n==1`. **Time:** `O(log n)`. **Space:** `O(1)`.
- **Optimized — Bitwise + modulo:** Check `n>0 and (n&(n-1))==0 and n%3==1`. The bitwise check confirms one set bit; the modulo check distinguishes powers of four from other powers of two. **Time:** `O(1)`*. **Space:** `O(1)`*.
- **Alternative (32-bit mask):** `n>0 and (n&(n-1))==0 and (n&0x55555555)!=0`; the mask checks that the single set bit appears in an even-numbered binary position (counting from zero). The mask is specific to 32-bit inputs.
- **Pattern recognition:** Power of four is a power of two with its one set bit in an even position.

**Dry run:** `64 → 16 → 4 → 1`, so return `True`. For the bitwise method, `64&63=0` and `64%3=1`.

---

## Key Differences to Remember

- **Power of Four:** A bitwise property plus modular arithmetic can replace repeated division.
- **Valid Perfect Square:** Binary search is possible because `mid*mid` increases as `mid` increases.
- **Base 4 Representation:** Extract remainders with `%4`, then reverse their order; output storage is required.
- **Check Perfect Number:** Proper divisors come in pairs; check only up to the square root.
- **Recursion vs iteration:** A loop avoids recursive call-stack overhead when it can express the same process.
- **No math-library shortcuts:** These solutions use division, modulo, multiplication, bitwise operations and manual iteration.


**Total covered: 4 problems — 1 primary + 3 variants.**
