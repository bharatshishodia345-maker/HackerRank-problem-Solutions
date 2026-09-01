# Non-Divisible Subset

## Problem

Given an integer `k` and an array `s`, find the maximum size of a subset such that the sum of any two numbers in the subset is **not divisible by `k`**.

## Approach

The solution uses the **remainder of each number when divided by `k`**.

For every number:

```python
num % k
```

we count how many numbers have each remainder.

For a remainder `r`, the complementary remainder is:

```text
k - r
```

because:

```text
r + (k - r) = k
```

So, elements from these two remainder groups cannot both be selected.

Therefore, for every pair of complementary remainders, we select the group with the larger frequency.

### Special Cases

* From remainder `0`, we can select at most **one** element.
* If `k` is even, from remainder `k/2`, we can also select at most **one** element.

## Complexity

* **Time:** `O(n + k)`
* **Space:** `O(k)`

## Example

```text
k = 3
s = [1, 7, 2, 4]

Remainders:

1 → [1, 7, 4]
2 → [2]

Choose the larger group → 3 elements

Answer: 3
```

## Solution

```python
def nonDivisibleSubset(k, s):
    remainder = [0] * k

    for num in s:
        remainder[num % k] += 1

    ans = 0

    if remainder[0] > 0:
        ans += 1

    for r in range(1, (k + 1) // 2):
        ans += max(remainder[r], remainder[k - r])

    if k % 2 == 0 and remainder[k // 2] > 0:
        ans += 1

    return ans
```
