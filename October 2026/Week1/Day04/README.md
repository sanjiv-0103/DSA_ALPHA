# Day 04 - Running Sum of 1D Array

| Problem | Approach | Time | Space |
|---|---|---|---|
| Running Sum of 1D Array | Prefix sum using running total | O(n) | O(1) |
| Build Array from Permutation | Create new array using nums[nums[i]] | O(n) | O(n) |
| Shuffle the Array | Combine first half and second half alternately | O(n) | O(n) |
| Richest Customer Wealth | Find sum of each row and maximum wealth | O(n × m) | O(1) |
| Left and Right Sum Differences | Brute force - calculate left and right sums for every index | O(n²) | O(n) |

## Key Points :
- Prefix sum keeps a running total of array elements
- Running sum can be calculated in one loop
- Array transformation problems create a new arrangement using indexes
- Brute force is simple to understand but can take more time
- Left and right sums can later be optimized using the prefix sum concept