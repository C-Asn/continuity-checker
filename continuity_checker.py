"""Activity 2: A simple continuity checker on the closed interval [0, 300]."""

import tkinter as tk


# 1. Calculate the electricity bill using the given piecewise function.
def f(x):
    if x < 100:
        return 10 * x
    elif x < 200:
        return 8 * x + 200
    else:
        return 7 * x + 300


# 2. Use the formula on the LEFT of x to find the exact left-hand limit.
def left_limit(x):
    if x <= 100:
        return 10 * x
    elif x <= 200:
        return 8 * x + 200
    else:
        return 7 * x + 300


# Convert usage and bill into screen coordinates (screen y increases downward).
def graph_point(x, y):
    return 50 + x, 220 - y / 12


def draw_graph(x):
    graph.delete("all")
    graph.create_line(50, 220, 375, 220, arrow=tk.LAST)
    graph.create_line(50, 220, 50, 10, arrow=tk.LAST)
    graph.create_text(210, 254, text="Usage x")
    graph.create_text(65, 10, text="Bill f(x)", anchor="w")
    for tick in [0, 100, 200, 300]:
        graph.create_text(50 + tick, 234, text=str(tick))
    for tick in [0, 1000, 2000]:
        graph.create_text(44, 220 - tick / 12, text=str(tick), anchor="e")

    # Draw each tier separately: do not join the jump at x = 200.
    for start_x, start_y, end_x, end_y in [
            (0, 0, 100, 1000), (100, 1000, 200, 1800), (200, 1700, 300, 2400)]:
        x1, y1 = graph_point(start_x, start_y)
        x2, y2 = graph_point(end_x, end_y)
        graph.create_line(x1, y1, x2, y2, fill="blue", width=2)

    # An open circle excludes (200, 1800); filled circles are actual values.
    for px, py, fill in [(100, 1000, "blue"), (200, 1800, "white"),
                         (200, 1700, "blue")]:
        sx, sy = graph_point(px, py)
        graph.create_oval(sx - 4, sy - 4, sx + 4, sy + 4, outline="blue", fill=fill)
    graph.create_text(258, 55, text="Jump at 200", anchor="w")
    sx, sy = graph_point(x, f(x))
    graph.create_line(sx, 220, sx, sy, fill="red", dash=(3, 3), tags="selected")
    graph.create_oval(sx - 6, sy - 6, sx + 6, sy + 6,
                      outline="red", width=2, tags="selected")


# 3. Read the input and display the continuity result.
def check():
    try:
        x = float(entry.get())
        if not 0 <= x <= 300:
            raise ValueError
    except ValueError:
        result.config(text="Please enter a number from 0 to 300.")
        graph.delete("selected")
        return

    value = f(x)
    left = left_limit(x)
    right = f(x)  # Each pricing tier includes its left endpoint.

    if x < 100:
        formula = "10x"
    elif x < 200:
        formula = "8x + 200"
    else:
        formula = "7x + 300"

    # At the endpoints, check only the limit from INSIDE [0, 300].
    if x == 0:
        continuous = right == value
        limits = f"Left limit: Not required at 0\nRight limit: {right:g}"
    elif x == 300:
        continuous = left == value
        limits = f"Left limit: {left:g}\nRight limit: Not required at 300"
    else:
        continuous = left == right == value
        limits = f"Left limit: {left:g}\nRight limit: {right:g}"

    if continuous:
        conclusion = "Continuous"
    else:
        conclusion = "NOT continuous (a jump in the bill)"

    result.config(text=f"Formula: {formula}\n{limits}\n"
                       f"f({x:g}) = {value:g}\nConclusion: {conclusion}")
    draw_graph(x)


# 4. Create the window, input box, button, and result label.
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Pricing Continuity Checker")

    tk.Label(window, text="Electricity Pricing: Interval [0, 300]",
             font=("Arial", 14, "bold")).pack(padx=20, pady=10)
    tk.Label(window, text="10x for 0 <= x < 100\n"
                         "8x + 200 for 100 <= x < 200\n"
                         "7x + 300 for x >= 200").pack()
    tk.Label(window, text="Enter usage x (try 100 and 200):").pack(pady=(10, 0))
    entry = tk.Entry(window)
    entry.pack(pady=5)
    entry.insert(0, "100")
    tk.Button(window, text="Check continuity", command=check).pack(pady=5)
    result = tk.Label(window, text="", justify="left", font=("Arial", 11))
    result.pack(padx=20, pady=10)

    bottom = tk.Frame(window)
    bottom.pack(padx=15, pady=5)
    graph = tk.Canvas(bottom, width=400, height=270, bg="white")
    graph.pack(side="left")
    table = "Usage x       Bill f(x)\n"
    for x in [0, 99, 100, 101, 199, 200, 201, 300]:
        table += f"{x:7}       {f(x):9}\n"
    tk.Label(bottom, text=table, font=("Consolas", 10), justify="left").pack(side="left", padx=10)
    tk.Label(window, text="Blue: pricing function | Red ring: selected point\n"
                         "Open circle: excluded value | Filled circle: included value").pack()
    tk.Label(window, text="The whole interval is NOT continuous: there is a jump at 200.",
             wraplength=380).pack(padx=20, pady=10)

    check()
    window.mainloop()
