# Day 23 - Baseball Game

| Problem | Approach | Time | Space |
|---|---|---|---|
| Baseball Game | Brute force - use stack and calculate total at the end | O(n) | O(n) |
| Baseball Game | Optimized - stack with running total | O(n) | O(n) |
| Build an Array With Stack Operations | Optimized - simulate operations without storing final array | O(n) | O(n) |

## Primary - Brute Force Logic
- Store valid scores in a stack.
- `C` removes the previous score.
- `D` adds double the previous score.
- `+` adds the previous two scores.
- Add all scores at the end.

## Primary - Optimized Logic
- Use a stack to store valid scores.
- Keep a running total.
- When adding a score, increase total.
- When removing a score, decrease total.
- No need to calculate the full sum again.

## Variant - Brute Force Logic
- Read numbers from `1` to `n`.
- Push every number.
- Pop values that are not needed.
- Stop when the target array is formed.

## Variant - Optimized Logic
- Simulate Push and Pop directly.
- Keep a pointer for the current target value.
- No need to store the final array.

## Key Point
Stack follows:
`LIFO - Last In First Out`