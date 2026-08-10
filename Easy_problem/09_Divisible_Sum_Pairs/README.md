# Divisible Sum Pairs

## Problem

Given an array of integers, find the number of pairs `(i, j)` such that:

- `i < j`
- `(ar[i] + ar[j])` is divisible by `k`

## Approach

- Use two nested loops to generate every possible pair.
- Calculate the sum of each pair.
- Check whether the sum is divisible by `k`.
- Increment the count when the condition is satisfied.

## Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

## HackerRank

Problem: Divisible Sum Pairs