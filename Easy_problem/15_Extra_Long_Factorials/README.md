# Extra Long Factorials

## 📌 Problem

Given an integer `n`, calculate and print `n!` (factorial of `n`).

Factorial is defined as:

n! = n × (n-1) × (n-2) × ... × 1

For example:

5! = 5 × 4 × 3 × 2 × 1 = 120

---

## 💡 Approach

Initialize `fact = 1`.

Then iterate from `1` to `n` and multiply each number with `fact`.

```python
fact = 1

for i in range(1, n + 1):
    fact = fact * i