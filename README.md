# Activity 2: Simple Python GUI

Run `python continuity_checker.py`. No extra packages are required.
Enter usage from 0 to 300, then click **Check continuity**.
The program uses the fixed closed interval [0, 300] to keep the code simple.

## How to explain the code

1. `f(x)` uses if/elif/else to choose the electricity pricing formula.
2. `left_limit(x)` selects the formula just before x and evaluates it at x.
   The `<=` signs matter: at 100 it uses 10x; at 200 it uses 8x + 200.
3. `check()` reads the input, finds the limits and function value, and compares
   them. At interior points, continuity requires left limit = right limit = f(x).
   Here the right limit equals f(x) because each tier includes its left endpoint.
   At 0 and 300, only the limit from inside the interval is required.
4. Tkinter creates the labels, input box, and button. `pack()` arranges them.
   Clicking the button runs `check()`, and `config()` updates the result.
5. A small loop creates a table of sample usage and bill values.
6. `draw_graph(x)` uses Tkinter Canvas to draw the three straight pricing lines.
   `graph_point(x, y)` converts mathematical coordinates to screen positions.
   The lines meet at 100, but there is a gap at 200. The open circle at
   (200, 1800) is excluded; the filled circle at (200, 1700) is the actual value.
   A red ring marks the entered point. No graphing packages are needed.

## Required demonstrations

| x | Left limit | Right limit | f(x) | Result |
| --- | --- | --- | --- | --- |
| 100 | 1000 | 1000 | 1000 | Continuous |
| 200 | 1800 | 1700 | 1700 | NOT continuous |

At 200, the bill drops by 100 units. This jump makes the function
not continuous on the entire interval [0, 300].

Limits are calculated directly from the linear formulas, avoiding the tiny-step
rounding and tolerance problem in the handout. The GUI rejects invalid input.
