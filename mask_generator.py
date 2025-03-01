import os
import math
import textwrap

head = """\
#ifndef MASKS
#define MASKS

#include <stdio.h>

typedef const uint8_t mask_array_t;
typedef const struct {
  const mask_array_t *mask_array;
  const char *name;
  const uint8_t height; 
  const uint8_t width; 
} mask_t;


"""

middle = """
static mask_t *const mask_table[] = {
"""

tail = """\
};

#endif
"""

def get_vals(path, f):
    error = False
    vals = {}

    text = f.read()
    try:
        vals["name"] = text[text.index("Name: ")+len("Name: "):text.index("\n", text.index("Name: "))]
        vals["name"] = vals["name"].replace("-", "_")
    except:
        print(f"{path}: error - improper formatting")
        return

    try:
        vals["order"] = int(text[text.index("Order: ")+len("Order: "):text.index("\n", text.index("Order: "))])
    except:
        print("Unimplemented - missing order")
        return
        # vals["order"] = len(masks)

    try:
        lines = text[text.index("\n", text.index("Mask:"))+1:].splitlines()
    except:
        print(f"{path}: error - improper formatting")
        return

    print(lines)
    result = ""
    if len(lines) == 0:
        print(f"{path}: error - text file is empty")
        return
    width = len(lines[0].strip())

    for line in lines:
        line = line.strip()
        # if(len(line) != width):
        #     print(f"{path}: error - text file does not contain a rectangular matrix")
        #     error = True
        #     return
        result = result + line

    print(result)
    vals["height"] = len(lines)
    vals["width"] = width
    split_list = textwrap.wrap(result, 8)
    split_string = ''.join(f"0b{s[::-1]}, " for s in split_list)
    vals["mask_array"] = f"""{{{split_string}}}"""
    # vals["mask_array"] = f"""{{{[f"0b{s}"[1:-1] for s in vals["mask_array"]].join()[1:-1]}}}]"""

    print(vals)
    return vals

def make_result(masks):
    mask_string = ""
    table_entries = ""
    for mask in masks:
        this_mask = f"""\
static mask_array_t mask_array_{mask["name"]}[] = {mask["mask_array"]};
static char mask_name_{mask["name"]}[] = "{mask["name"]}";
static mask_t mask_{mask["name"]} = {{mask_array_{mask["name"]}, mask_name_{mask["name"]}, {mask["height"]}, {mask["width"]}}};\n\n"""
        mask_string = mask_string + this_mask

        this_table_entry = f"""\t&mask_{mask["name"]},\n""" 
        table_entries = table_entries + this_table_entry
    return head + mask_string + middle + table_entries + tail

def main():
    files = os.listdir("masks")

    masks = []

    for path in files:
        if path.endswith(".txt"):  # Ensure it's a text file
            with open(f"masks/{path}") as f:
                vals = get_vals(path, f)
                if vals is not None:
                    masks.append(vals)

    masks.sort(key=lambda x: x["order"])

    result = make_result(masks)
    print(result)

    with open(f"output/mask_patterns.h", "w+") as f:
        f.write(result)

    print("See output for results")  # add a verbose mode?


if __name__ == "__main__":
    main()
