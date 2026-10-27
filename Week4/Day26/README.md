# Day 26 - Next Greater Element I

| Problem | Approach | Time | Space |
|---|---|---|---|
| Next Greater Element I | Brute force - search after each element for first greater value | O(n*m) | O(n) |
| Daily Temperatures | Brute force - check future temperatures | O(n²) | O(n) |
| Daily Temperatures | Optimized - monotonic stack using indexes | O(n) | O(n) |

## Primary - Brute Force Logic
- Take each value from `nums1`.
- Find it inside `nums2`.
- Search the values after it.
- Return the first greater value.
- If no greater value exists, return `-1`.

## Variant - Brute Force Logic
- Check every temperature.
- Search the days after it.
- Stop when the first warmer day is found.
- Store the difference between the indexes.

## Variant - Optimized Logic
- Store temperature indexes in a stack.
- If the current temperature is warmer than the stack top temperature, pop the old index.
- Calculate the number of days using the index difference.