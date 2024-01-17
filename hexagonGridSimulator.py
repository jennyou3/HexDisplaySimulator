import tkinter as tk
import math

def draw_mini_hexagon(canvas, x, y, size):
    angle = 60
    coordinates = []

    for _ in range(6):
        x = x + size * math.cos(math.radians(angle))
        y = y + size * math.sin(math.radians(angle))
        coordinates.extend([x, y])
        angle += 60

    # Connect the last point to the first point to close the hexagon
    coordinates.extend([coordinates[0], coordinates[1]])
    
    canvas.create_line(coordinates, fill="black")

def main():
    root = tk.Tk()
    root.title("Mini Hexagon Drawing")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # Coordinates and size for the mini hexagon
    mini_hexagon_y = 50
    mini_hexagon_size = 10
        
    sizes = [8,9,10,11,12,13,14,15,14,13,12,11,10,9,8]
    count = 0

    x_starts = 100
    y_starts = [120, 110, 100, 90, 80, 70, 60, 50, 60, 70, 80, 90, 100, 110, 120]
    for s in sizes:
        mini_hexagon_y = y_starts[count]

        for j in range(s):
            draw_mini_hexagon(canvas, x_starts, mini_hexagon_y, mini_hexagon_size)
            mini_hexagon_y += 20     
        x_starts += 17
        print(count)
        count +=1
        
    root.mainloop()

if __name__ == "__main__":
    main()
