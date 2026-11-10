
# November DSA — Day 9

**Topic:** Linked Lists, Pointer Manipulation, Iteration and Recursion  

## Complexity Summary

| # | Problem | Approach | Time | Auxiliary Space |
|---|---|---|---|---|
| Primary | Reverse Linked List (LC 206) | Iterative reversal using three pointers | `O(n)` | `O(1)` |
| Primary | Reverse Linked List (LC 206) | Recursive reversal during call-stack unwinding | `O(n)` | `O(n)` |
| Variant 1 | Print Linked List in Reverse | Repeated iterative traversal (baseline) | `O(n²)` | `O(1)` |
| Variant 1 | Print Linked List in Reverse | Recursive printing during stack unwinding | `O(n)` | `O(n)` |
| Variant 1 | Print Linked List in Reverse | Iterative traversal using an explicit stack | `O(n)` | `O(n)` |
| Variant 2 | Reverse a Doubly Linked List | Iterative swapping of prev and next pointers | `O(n)` | `O(1)` |
| Variant 2 | Reverse a Doubly Linked List | Recursive swapping of prev and next pointers | `O(n)` | `O(n)` |


---

## Primary — Reverse Linked List (LC 206)

**Problem:** Given the head of a singly linked list, reverse its node connections and return the new head.

**Example:**

Input: `1 → 2 → 3 → 4 → None`

Output: `4 → 3 → 2 → 1 → None`

### Approach 1 — Iterative Reversal (Optimized)

- Initialize `prev=None` and `curr=head`.
- Store the next node using `nxt=curr.next`.
- Reverse the current pointer using `curr.next=prev`.
- Move `prev` to `curr`.
- Move `curr` to `nxt`.
- Repeat until `curr` becomes `None`.
- Return `prev` as the new head.
- **Time:** `O(n)`.
- **Space:** `O(1)`.

**Pointer logic:**

```python
nxt=curr.next
curr.next=prev
prev=curr
curr=nxt
```

**Memory trick:** Save → Reverse → Move → Move.

### Approach 2 — Recursive Reversal

- Return `head` if the list is empty or contains one node.
- Recursively reverse the remaining list.
- Use `head.next.next=head` to reverse the connection.
- Set `head.next=None` to remove the original forward link.
- Return the new head obtained from recursion.
- **Time:** `O(n)`.
- **Space:** `O(n)` due to recursive calls.

**Important operations:**

```python
head.next.next=head
head.next=None
```

---


## Key Differences to Remember

- **Reverse Linked List:** Changes actual `next` pointers and returns the new head.
- **Print Linked List in Reverse:** Does not modify links; only changes the printing order.
- **Reverse Doubly Linked List:** Swaps both `prev` and `next` pointers at every node.
- **Iterative Singly Linked List Reversal:** Uses `prev`, `curr`, and `nxt`.
- **Recursive Singly Linked List Reversal:** Uses the call stack to reverse pointers while returning.
- **Recursive Reverse Printing:** Prints values after recursive calls.
- **Doubly Linked List Reversal:** After swapping pointers, move using `curr.prev`.
- **Space Optimization:** Iterative pointer reversal requires `O(1)` auxiliary space, while recursion requires `O(n)` stack space.
- **Pointer Safety:** Always preserve the remaining list before changing a singly linked list's `next` pointer.

---

## Singly vs Doubly Linked List

| Feature | Singly Linked List | Doubly Linked List |
|---|---|---|
| Node references | `next` | `prev` and `next` |
| Traversal | Forward | Forward and backward |
| Reversal technique | Redirect `next` pointers | Swap `prev` and `next` |
| Main iterative variables | `prev`, `curr`, `nxt` | `curr`, `newHead` |
| Iterative time | `O(n)` | `O(n)` |
| Iterative auxiliary space | `O(1)` | `O(1)` |


---

## Day 9 Completion

- [x] Primary — Reverse Linked List (Iterative + Recursive)
- [x] Variant 1 — Print Linked List in Reverse (Repeated Traversal + Recursion + Stack)
- [x] Variant 2 — Reverse a Doubly Linked List (Iterative + Recursive)
