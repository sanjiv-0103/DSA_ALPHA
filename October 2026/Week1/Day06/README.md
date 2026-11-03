# Day 06 - Find All Numbers Disappeared in an Array

| Problem | Approach | Time | Space |
|---|---|---|---|
| Find All Numbers Disappeared in an Array | In-place marking using negative values | O(n) | O(1) |
| Missing Number | Compare expected sum with actual sum | O(n) | O(1) |
| Set Mismatch | Brute force - find duplicate and missing number | O(n²) | O(1) |

## Key Points
- In-place marking uses the same array to track present numbers.
- Positive positions after marking represent missing numbers.
- Missing Number uses the difference between expected and actual sum.
- Set Mismatch finds one duplicate and one missing value.