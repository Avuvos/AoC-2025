# Day 06

## Part 1

Parse by splitting each line on whitespace — numbers align into columns.

For each column, grab all numbers and apply the operator from the bottom row (`+` or `*`). Sum the results.

### Time Complexity

`O(n × m)` where n = rows, m = columns.

## Part 2

Now parse character-by-character. Pad lines to equal length, then transpose the grid so columns become strings.

Use `groupby` to split columns into problem blocks (separated by all-space columns).

Within each block, read columns right-to-left — each column forms a number with digits top-to-bottom. The operator is in the last row (`c[-1]`).

### Time Complexity

`O(n × m)` — transpose is the main work.
