# Day 10

Button matrix problem: Part 1 is binary XOR, Part 2 transforms into Mixed Integer Linear Programming.

## Part 1

Given an initial binary state and a set of buttons (each toggling specific positions), find the minimum number of button presses to turn all lights off.

**Approach:** BFS over binary states. Represent state as an integer, precompute each button as a bitmask, then XOR to apply. Track visited states to avoid cycles.

**Key optimization:** Precompute button masks so each press is a single XOR operation instead of bit-by-bit.

### Time Complexity

`O(2^n × b)` where n = light positions, b = number of buttons.

## Part 2

Now each button press adds to output voltages (not toggles), and we're given target voltages. Find button presses that achieve the target with minimum total presses.

**The insight:** This is a linear algebra problem `Ax = b`:

```
                    (0 0 0 1)
                    (0 1 0 1)
(x1 x2 x3 x4 x5 x6) (0 0 1 0) = (3, 5, 4, 7)
                    (0 0 1 1)
                    (1 0 1 0)
                    (1 1 0 0)
```

- Each matrix row = a button (1s indicate which output positions it affects)
- Each `x_i` = times button `i` is pressed
- `b` = target voltage vector

We need: `Ax = b`, `x ≥ 0`, `x ∈ Z`, minimize `sum(x)`.

This is exactly **Mixed Integer Linear Programming** (MILP) with L1 minimization. Use `scipy.optimize.milp` which handles integer constraints via branch-and-bound with LP relaxations.

### Time Complexity

Polynomial in practice due to problem structure (0-1 matrix, bounded solution space).

