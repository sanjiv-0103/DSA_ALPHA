# Day 4

**Problems covered:** 1 primary + 2 variants  

## Complexity Summary

| # | Problem | Brute / Approach 1 | Brute Time | Brute Space | Optimized / Approach 2 | Optimized Time | Optimized Space |
|---|---|---|---|---|---|---|---|
| Primary | Power of Three  | Recursive division by 3 | `O(log n)` | `O(log n)` | Iterative division by 3 | `O(log n)` | `O(1)` |
| Variant 1 | Base 3 Digits of a Number | Recursive conversion using string concatenation | `O(d²)` | `O(d²)` upper bound | Iterative digit extraction with manual reversal | `O(d)` | `O(d)` |
| Variant 2 | Sum of Digits in Base K  | Recursively extract and add digits | `O(logₖ n)` | `O(logₖ n)` | Iterative digit extraction and accumulation | `O(logₖ n)` | `O(1)` |

---

## Primary — Power of Three 

**Problem:** Given an integer `n`, return `True` if `n` is a power of 3. Otherwise, return `False`.

**Examples:** `27 → True`, `45 → False`, `1 → True`.

### Approach 1 — Recursion

- Check whether `n==1`. If true, return `True`.
- Return `False` when `n<=0` or `n%3!=0`.
- Otherwise, recursively check `n//3`.
- **Time:** `O(log n)`.
- **Space:** `O(log n)` for the recursive call stack.

### Approach 2 — Iteration (Optimized)

- Return `False` for nonpositive numbers.
- Repeatedly divide `n` by 3 while `n%3==0`.
- Return whether the remaining number equals 1.
- Avoids recursive stack memory.
- **Time:** `O(log n)`.
- **Space:** `O(1)`.

**Dry run:** `81 → 27 → 9 → 3 → 1 → True`.

**Pattern recognition:** A number is a power of a fixed base when repeated exact division by that base reduces it to 1.

---

## Variant 1 — Base 3 Digits of a Number

**Problem:** Convert a nonnegative decimal integer into its base-3 representation as a string.

**Examples:** `10 → "101"`, `15 → "120"`, `0 → "0"`.

### Brute / Recursive Approach

- If `n<3`, return `str(n)`.
- Otherwise, recursively convert `n//3`.
- Append `str(n%3)` to construct the base-3 representation.
- **Time:** `O(d²)` due to repeated string concatenation.
- **Space:** `O(d²)` peak upper bound including temporary strings and recursive frames.

### Optimized / Iterative Approach

- Handle `n==0` by returning `"0"`.
- Extract each digit using `n%3`.
- Store the extracted digits in a list.
- Remove each digit using `n//=3`.
- Reverse the list manually using two pointers.
- Join the digits into the final string.
- **Time:** `O(d)`.
- **Space:** `O(d)`.

**Dry run:** `n=15` produces remainders `0,2,1`. Reversing gives `"120"`.

**Pattern recognition:** Modulo extracts the last digit of a number in a given base; integer division removes that digit.

---

## Variant 2 — Sum of Digits in Base K

**Problem:** Given a positive integer `n` and a base `k`, return the sum of the digits of `n` in base `k`.

**Example:** `n=34, k=6 → 9`, because `34` is `54` in base 6 and `5+4=9`.

**Recurrence:** `S(n,k)=n%k+S(n//k,k)`.

**Base case:** `S(0,k)=0`.

### Brute / Recursive Approach

- If `n==0`, return `0`.
- Extract the last digit using `n%k`.
- Recursively calculate the digit sum of `n//k`.
- Add the current digit to the recursive result.
- **Time:** `O(logₖ n)`.
- **Space:** `O(logₖ n)` due to the recursion stack.

### Optimized / Iterative Approach

- Initialize `total=0`.
- Repeatedly extract the last digit using `n%k`.
- Add the extracted digit directly to `total`.
- Remove the processed digit using `n//=k`.
- Return the accumulated sum.
- **Time:** `O(logₖ n)`.
- **Space:** `O(1)`.

**Dry run:** `n=34, k=6`: extract `4`, then `5`; total `4+5=9`.

**Pattern recognition:** When only the digit sum is required, accumulate remainders directly instead of constructing the converted number.

---

## Key Differences to Remember

- **Power of Three:** Repeatedly divide by 3 and verify that the final value is 1.
- **Base 3 Digits:** Extract and store digits. Order matters, so reverse them during iterative conversion.
- **Sum of Digits in Base K:** Extract digits and add them directly. Digit order does not matter.
- **Recursion vs Iteration:** Both use division and modulo, but iteration avoids recursive call-stack memory.
- **Space Optimization:** Base conversion requires storage for the output digits, whereas digit summation needs only a running total.

---
