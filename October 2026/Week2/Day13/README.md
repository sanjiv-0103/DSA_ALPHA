# Day 13 - Maximum Average Subarray I

| Problem | Approach | Time | Space |
|---|---|---|---|
| Maximum Average Subarray I | Optimized sliding window using running sum | O(n) | O(1) |
| Max Sum Subarray of Size K | Optimized sliding window using running sum | O(n) | O(1) |
| Kids With the Greatest Number of Candies | Find maximum, then compare each value with extra candies | O(n) | O(n) |

## Key Points
- Sliding window keeps a fixed-size window.
- Add the new value and remove the old value.
- Running sum avoids recalculating every window.
- Variant 2 checks whether each can reach the current maximum.