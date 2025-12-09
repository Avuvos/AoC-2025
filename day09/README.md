# Day 09

Rectangle selection problem with a twist: Part 2 requires checking if rectangles lie entirely within a polygon.

## Part 1

Given a list of red tile coordinates, find the largest axis-aligned rectangle using any two red tiles as opposite corners. Simply iterate all pairs and track the maximum area.

### Time Complexity

`O(n²)` for checking all pairs.

## Part 2

Now rectangles must only contain red or green tiles:
- Red tiles = the input points
- Green tiles = boundary lines connecting consecutive red points AND the interior of the polygon

The interior being green is the key insight—it's not just the boundary that's valid.

### Coordinate Compression

The grid can be billions of cells, but the polygon structure only changes at x/y values where red points exist.

**Example:**
- Original points: `[(2, 5), (7, 5), (7, 1), (11, 1)]`
- Unique x values: `[2, 7, 11]` → map to indices `[1, 2, 3]` (1-indexed for padding)
- Unique y values: `[1, 5]` → map to indices `[1, 2]`
- Compressed points: `[(1, 2), (2, 2), (2, 1), (3, 1)]`

**Why this works:** The input defines a polygon by connecting consecutive points in order. Compression changes coordinates but preserves:
1. The order of points (polygon shape)
2. Which points share the same row/column (line connectivity)

If point A and B are on the same row in the original, they're on the same row in compressed space. So drawing lines between consecutive compressed points creates the same polygon structure.

### Finding Interior Cells

After drawing boundary lines, we need to mark interior cells as valid:

1. Padding is built into compression (indices start at 1)—this guarantees `(0,0)` is outside the polygon
2. BFS from `(0,0)` to find all exterior cells
3. Build prefix sum where interior/boundary = `1`, exterior = `0`

### Checking Rectangles

For each pair of red points as corners:
1. Map to compressed coordinates
2. Query prefix sum for that rectangle
3. If sum equals the rectangle area (all cells are `1`), it's valid
4. Track the **real area** using original coordinates

### Time Complexity

`O(n²)` where n = number of red tiles. Compressed grid is at most n×n, prefix sum queries are O(1).

