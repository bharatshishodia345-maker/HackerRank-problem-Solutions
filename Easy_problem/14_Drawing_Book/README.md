# Drawing Book

## 📌 Problem

A book has `n` pages and the user wants to turn to page `p`.

The book can be opened from either the front or the back.

Find the minimum number of page turns required to reach page `p`.

---

## 💡 Approach

Calculate the number of turns from both directions.

### From Front

```python
front = p // 2