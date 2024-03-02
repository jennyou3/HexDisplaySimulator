import tkinter as tk
import math
import os

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
        current_fill = canvas.itemcget(hexagon_tag, "fill")
        
        if current_fill == "hotpink":
            canvas.itemconfig(hexagon_tag, fill="")
            clicked_hexagons[hexagon_tag] = 0
        else:
            canvas.itemconfig(hexagon_tag, fill="hotpink")
            clicked_hexagons[hexagon_tag] = 1  

def get_clicked_state_string():
    return ''.join(str(clicked_hexagons.get(tag, 0)) for tag in clicked_hexagons)

def save_state_to_file():
    name = input("Enter the name: ")
    order = input("Enter the order: ")
    file_name = input("Enter the desired file name (without extension): ")
    
    clicked_state_string = get_clicked_state_string()
    substring_array = [clicked_state_string[i:i+8] for i in range(0, len(clicked_state_string), 8)]

    mask_folder_path = "masks"
    file_path = os.path.join(mask_folder_path, f"{file_name}.txt")
    with open(file_path, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Order: {order}\n")
        file.write("\n")
        file.write("Mask:\n")
        for substring in substring_array:
            file.write(substring + '\n')

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
            clicked_hexagons[tag] = 0  

        x_starts += 17
        count += 1

    canvas.bind("<Button-1>", change_hexagon_color)

    save_button = tk.Button(root, text="Save State to File", command=save_state_to_file)
    save_button.pack()

    root.mainloop()

if __name__ == "__main__":
    clicked_hexagons = {}  
    main()
