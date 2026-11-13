
# November DSA — Day 11

**Problems covered:** 1 primary + 2 variants  

## Complexity Summary

| # | Problem | Brute-force / Baseline approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Linked List Cycle (LC 141) | Bounded traversal using maximum node-count constraint | `O(B)` | `O(1)` | Floyd's fast and slow pointer cycle detection | `O(n)` | `O(1)` |
| Variant 1 | Linked List Cycle II (LC 142) | Bounded pointer traversal with repeated reference checking | `O(B²)` upper bound | `O(1)` | Floyd's cycle detection followed by cycle-start identification | `O(n)` | `O(1)` |
| Variant 2 | Happy Number (LC 202) | Repeated digit-square calculation until reaching 1 or the known unhappy cycle value 4 | `O(d)` | `O(1)` | Floyd's cycle detection on the digit-square sequence | `O(d)` | `O(1)` |


---

## Primary — Linked List Cycle (LC 141)

**Problem:** Given the head of a singly linked list, determine whether it contains a cycle.

**Examples:**

- `1 → 2 → 3 → None` → `False`
- `1 → 2 → 3 → 2 → ...` → `True`
- A single node pointing to itself → `True`

### Approach 1 — Bounded Traversal (Baseline)

- Initialize `curr=head`.
- Traverse using `curr=curr.next`.
- Use the problem's maximum node-count constraint as a traversal bound.
- If `curr` reaches `None`, return `False`.
- If traversal continues beyond the maximum number of distinct permitted nodes, return `True`.
- This method depends on knowing the maximum possible list length.
- **Time:** `O(B)`.
- **Space:** `O(1)`.

**Limitation:** This is a constraint-specific baseline, not a general cycle detection technique.

### Approach 2 — Floyd's Cycle Detection (Optimized)

- Initialize `slow=head` and `fast=head`.
- Move slow one step and fast two steps.
- Continue while `fast` and `fast.next` exist.
- If slow and fast reference the same node, return `True`.
- If fast reaches the end, return `False`.
- No additional node storage is required.
- **Time:** `O(n)`.
- **Space:** `O(1)`.



```
