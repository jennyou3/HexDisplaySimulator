import tkinter as tk
import math

def draw_mini_hexagon(canvas, x, y, size, tag):
    angle = 60
    coordinates = []

    for _ in range(6):
        x = x + size * math.cos(math.radians(angle))
        y = y + size * math.sin(math.radians(angle))
        coordinates.extend([x, y])
        angle += 60

    canvas.create_polygon(coordinates, outline="black", fill="", tags=tag)

def change_hexagon_color(event):
    hexagon_tags = canvas.gettags(tk.CURRENT)

    if hexagon_tags:
        hexagon_tag = hexagon_tags[0]
        canvas.itemconfig(hexagon_tag, fill="red")
        clicked_hexagons[hexagon_tag] = 1  # Update the clicked state in the list

def get_clicked_state_string():
    # Convert the list of clicked states into a string
    return ''.join(str(clicked_hexagons.get(tag, 0)) for tag in (clicked_hexagons))

def main():
    root = tk.Tk()
    root.title("Interactive Hexagons")

    global canvas
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    mini_hexagon_y = 50
    mini_hexagon_size = 10

    sizes = [8, 9, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11, 10, 9, 8]
    count = 0

    x_starts = 100
    y_starts = [120, 110, 100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100, 110, 120]

    for s in sizes:
        mini_hexagon_y = y_starts[count]

        for j in range(s):
            tag = f"hexagon_{count}_{j}"
            draw_mini_hexagon(canvas, x_starts, mini_hexagon_y, mini_hexagon_size, tag)
            mini_hexagon_y += 20
            clicked_hexagons[tag] = 0  # Initialize clicked state to 0

        x_starts += 17
        count += 1

    canvas.bind("<Button-1>", change_hexagon_color)

    # Add a button to print the clicked state string
    button = tk.Button(root, text="Print Clicked State", command=print_clicked_state)
    button.pack()

    root.mainloop()

def print_clicked_state():
    clicked_state_string = get_clicked_state_string()
    print(clicked_state_string)

if __name__ == "__main__":
    clicked_hexagons = {}  # Dictionary to store clicked state of each hexagon
    main()
