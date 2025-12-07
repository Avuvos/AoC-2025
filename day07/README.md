# Day 07

Classic grid traversal problem. Both parts use caching, but in fundamentally different ways.

## Part 1

Simulate the tachyon beam: start from `S`, move downward. On a splitter (`^`), recurse left and right, counting the split.

Key insight: mark visited cells with `|` to avoid double-counting. If a beam reaches an already-visited cell, return early since that path was already counted by another beam.

### Time Complexity

`O(n × m)` where n, m = grid dimensions. Each cell visited at most once.

## Part 2

Now we count *timelines*, not splits. A particle takes both paths at each splitter, creating exponential branching.

Use `@cache` on `(i, j)` to memoize timeline counts from each cell. The key difference from Part 1: even if we reach the same cell from different directions, each arrival represents a unique timeline that followed a different path to get there. So we *want* the cached result added to our count, not skipped.

Base case: reaching the bottom row means 1 complete timeline.

### Time Complexity

`O(n × m)` with memoization. Each `(i, j)` computed once, lookups are `O(1)`.

