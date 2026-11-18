
# November DSA — Day 12

**Topic:** Linked Lists, Two-Pointer Merging, Pointer Rewiring, Sorting and Greedy Algorithms  

## Complexity Summary

| # | Problem | Brute-force / Baseline approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Merge Two Sorted Lists (LC 21) | Recursive comparison and merging using existing nodes | `O(m+n)` | `O(m+n)` | Iterative two-pointer merge with head and tail | `O(m+n)` | `O(1)` |
| Variant 1 | Merge Two Sorted Doubly Linked Lists | Recursive merging with next and prev pointer updates | `O(m+n)` | `O(m+n)` | Iterative merging with bidirectional pointer rewiring | `O(m+n)` | `O(1)` |
| Variant 2 | Merge Intervals (LC 56) | Repeated pair comparisons and merging | `O(n³)` upper bound | `O(n)` | Sorting followed by greedy interval merging | `O(n log n)` | `O(n)` |


---
