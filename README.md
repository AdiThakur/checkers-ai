## Checkers AI

This `python` script uses the `minimax` algorithm with `alpha-beta` pruning to determine the next best move given a starting checkers configuration. It can be invoked by running the following command:

```
python3 checkers.py <input file> <output file>
```

**Note** that the AI always plays as red.

---

#### Input Format

`<input file>` is a plain text file that contains eight lines. Each such line will represent a row of the checkers board, with 8 characters in each row. There are 5 possible values for these characters:

- `r` denotes a red piece
- `b` denotes a black piece
- `R` denotes a red king
- `B` denotes a black king
- `.` denotes an empty square

The following is an example of an input file in the aforementioned format:
```
........
....b...
.......R
..b.b...
...b...r
........
...r....
....B...
```

---

#### Output Format

The output format is exactly the same as the input specification.