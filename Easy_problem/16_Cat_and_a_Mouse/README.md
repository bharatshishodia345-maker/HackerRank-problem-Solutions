# Cat and a Mouse

## Problem

Given the positions of Cat A, Cat B, and Mouse C on a number line, determine which cat will reach the mouse first.

- If Cat A is closer, return `Cat A`.
- If Cat B is closer, return `Cat B`.
- If both cats are at the same distance, return `Mouse C`.

## Approach

Calculate the absolute distance of both cats from the mouse.

```python
distance_a = abs(z - x)
distance_b = abs(z - y)