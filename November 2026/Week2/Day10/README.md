
# November DSA — Day 10

**Problems covered:** 1 primary + 2 variants  

## Complexity Summary

| # | Problem | Brute-force approach | Brute time | Brute space | Optimized approach | Optimized time | Optimized space |
|---|---|---|---|---|---|---|---|
| Primary | Middle of the Linked List (LC 876) | Count nodes, then traverse to the middle | `O(L)` | `O(1)` | Fast and slow pointers moving at different speeds | `O(L)` | `O(1)` |
| Variant 1 | Nth Node from End of Linked List | Count nodes, then move `count-n` steps | `O(L)` | `O(1)` | Maintain an n-node gap between two pointers | `O(L)` | `O(1)` |
| Variant 2 | Remove Nth Node from End of List (LC 19) | Count nodes, find predecessor and bypass target | `O(L)` | `O(1)` | Two-pointer fixed gap with dummy node | `O(L)` | `O(1)` |


---

## Primary — Middle of the Linked List (LC 876)

**Problem:** Given the head of a singly linked list, return its middle node. If the list has two middle nodes, return the second middle node.

**Examples:**

- `1 → 2 → 3 → 4 → 5` → Middle node `3`
- `1 → 2 → 3 → 4 → 5 → 6` → Middle node `4`

### Approach 1 — Brute-force Two-Pass Counting

- Initialize `count=0`.
- Traverse the linked list and count all nodes.
- Calculate the middle position using `count//2`.
- Start another traversal from the head.
- Move forward `count//2` times.
- Return the current node.
- **Time:** `O(L)`.
- **Space:** `O(1)`.

### Approach 2 — Optimized Fast and Slow Pointers

- Initialize `slow=head` and `fast=head`.
- Move `slow` one node per iteration.
- Move `fast` two nodes per iteration.
- Continue while `fast` and `fast.next` exist.
- When fast reaches the end, slow points to the middle node.
- For even-length lists, the second middle node is returned.
- **Time:** `O(L)`.
- **Space:** `O(1)`.

---

