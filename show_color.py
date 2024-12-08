"""
Reverse Color Mapping for PyMOL

This script provides a reverse mapping of RGB tuples to color names for use in PyMOL.
It includes two comprehensive dictionaries:
1. `reverse_simple_named_colors`: Maps RGB values of common named colors (e.g., "red", "blue").
2. `reverse_chemical_element_colors`: Maps RGB values of colors associated with chemical elements.

Functionality:
- The script enables querying color names dynamically from their RGB tuples.
- It includes a utility function, `get_color_name_from_rgb(rgb)`, to retrieve the name of a color.
- The `label_colors_with_names` function labels PyMOL objects or residues with their respective color names.

Key Features:
- Combines simple named colors and chemical element colors into a unified dictionary (`combined_reverse_colors`).
- Labels residues or atoms dynamically in PyMOL based on their RGB values.
- Provides a PyMOL command `show_color` for easy integration.

Usage:
1. Load the script in PyMOL:
   run <script_name>.py
2. Use the `show_color` command in PyMOL to label residues or objects with their color names.

Example:
- Given an object with RGB `(1.0, 0.0, 0.0)`:
  - The script will label the corresponding residue with "red".

Dependencies:
- This script requires PyMOL's `cmd` module to function correctly.

Customization:
- Add more colors or chemical elements to the respective dictionaries as needed.
- Ensure RGB values are rounded to two decimal places to match PyMOL's precision.

Author:
 Koya Sakuma
 Github: @yakomaxa

License:
 MIT

Copyright (c) 2024 Koya Sakuma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from pymol import cmd, stored


# Making reverse tables to lookup RGB -> color name; see  https://pymolwiki.org/index.php/Color_Values

reverse_simple_named_colors = {
    (0.5, 1.0, 1.0): "aquamarine",
    (0.0, 0.0, 0.0): "black",
    (0.0, 0.0, 1.0): "blue",
    (0.85, 0.85, 1.0): "bluewhite",
    (0.1, 0.1, 1.0): "br0",
    (0.2, 0.1, 0.9): "br1",
    (0.3, 0.1, 0.8): "br2",
    (0.4, 0.1, 0.7): "br3",
    (0.5, 0.1, 0.6): "br4",
    (0.6, 0.1, 0.5): "br5",
    (0.7, 0.1, 0.4): "br6",
    (0.8, 0.1, 0.3): "br7",
    (0.9, 0.1, 0.2): "br8",
    (1.0, 0.1, 0.1): "br9",
    (1.0, 0.7, 0.2): "brightorange",
    (0.65, 0.32, 0.17): "brown",
    (0.2, 1.0, 0.2): "carbon",
    (0.5, 1.0, 0.0): "chartreuse",
    (0.555, 0.222, 0.111): "chocolate",
    (0.0, 1.0, 1.0): "cyan",
    (0.73, 0.55, 0.52): "darksalmon",
    (1.0, 1.0, 0.0): "dash",
    (0.25, 0.25, 0.65): "deepblue",
    (0.6, 0.6, 0.1): "deepolive",
    (0.6, 0.1, 0.6): "deeppurple",
    (1.0, 0.42, 0.42): "deepsalmon",
    (0.1, 0.6, 0.6): "deepteal",
    (0.1, 0.1, 0.6): "density",
    (0.7, 0.5, 0.5): "dirtyviolet",
    (0.698, 0.13, 0.13): "firebrick",
    (0.2, 0.6, 0.2): "forest",
    (0.5, 0.5, 0.5): "gray",
    (0.0, 1.0, 0.0): "green",
    (0.25, 1.0, 0.75): "greencyan",
    (1.0, 0.0, 0.5): "hotpink",
    (0.9, 0.9, 0.9): "hydrogen",
    (0.75, 0.75, 1.0): "lightblue",
    (1.0, 0.2, 0.8): "lightmagenta",
    (1.0, 0.8, 0.5): "lightorange",
    (1.0, 0.75, 0.87): "lightpink",
    (0.4, 0.7, 0.7): "lightteal",
    (0.5, 1.0, 0.5): "lime",
    (0.0, 1.0, 0.5): "limegreen",
    (0.75, 1.0, 0.25): "limon",
    (1.0, 0.0, 1.0): "magenta",
    (0.0, 0.5, 1.0): "marine",
    (0.2, 0.2, 1.0): "nitrogen",
    (0.77, 0.7, 0.0): "olive",
    (1.0, 0.5, 0.0): "orange",
    (1.0, 0.3, 0.3): "oxygen",
    (0.8, 1.0, 1.0): "palecyan",
    (0.65, 0.9, 0.65): "palegreen",
    (1.0, 1.0, 0.5): "paleyellow",
    (1.0, 0.65, 0.85): "pink",
    (0.75, 0.0, 0.75): "purple",
    (0.5, 0.0, 1.0): "purpleblue",
    (0.7, 0.3, 0.4): "raspberry",
    (1.0, 0.0, 0.0): "red",
    (0.6, 0.2, 0.2): "ruby",
    (1.0, 0.6, 0.6): "salmon",
    (0.72, 0.55, 0.3): "sand",
    (0.2, 0.5, 0.8): "skyblue",
    (0.5, 0.5, 1.0): "slate",
    (0.55, 0.7, 0.4): "smudge",
    (0.52, 0.75, 0.0): "splitpea",
    (0.9, 0.775, 0.25): "sulfur",
    (0.0, 0.75, 0.75): "teal",
    (0.3, 0.3, 1.0): "tv_blue",
    (0.2, 1.0, 0.2): "tv_green",
    (1.0, 0.55, 0.15): "tv_orange",
    (1.0, 0.2, 0.2): "tv_red",
    (1.0, 1.0, 0.2): "tv_yellow",
    (1.0, 0.5, 1.0): "violet",
    (0.55, 0.25, 0.6): "violetpurple",
    (0.85, 0.2, 0.5): "warmpink",
    (0.99, 0.82, 0.65): "wheat",
    (1.0, 1.0, 1.0): "white",
    (1.0, 1.0, 0.0): "yellow",
    (1.0, 0.87, 0.37): "yelloworange",
}
reverse_chemical_element_colors = {
    (0.439, 0.671, 0.980): "actinium",
    (0.749, 0.651, 0.651): "aluminum",
    (0.329, 0.361, 0.949): "americium",
    (0.620, 0.388, 0.710): "antimony",
    (0.502, 0.820, 0.890): "argon",
    (0.741, 0.502, 0.890): "arsenic",
    (0.459, 0.310, 0.271): "astatine",
    (0.000, 0.788, 0.000): "barium",
    (0.541, 0.310, 0.890): "berkelium",
    (0.761, 1.000, 0.000): "beryllium",
    (0.620, 0.310, 0.710): "bismuth",
    (0.878, 0.000, 0.220): "bohrium",
    (1.000, 0.710, 0.710): "boron",
    (0.651, 0.161, 0.161): "bromine",
    (1.000, 0.851, 0.561): "cadmium",
    (0.239, 1.000, 0.000): "calcium",
    (0.631, 0.212, 0.831): "californium",
    (0.200, 1.000, 0.200): "carbon",
    (1.000, 1.000, 0.780): "cerium",
    (0.341, 0.090, 0.561): "cesium",
    (0.122, 0.941, 0.122): "chlorine",
    (0.541, 0.600, 0.780): "chromium",
    (0.941, 0.565, 0.627): "cobalt",
    (0.784, 0.502, 0.200): "copper",
    (0.471, 0.361, 0.890): "curium",
    (0.900, 0.900, 0.900): "deuterium",
    (0.820, 0.000, 0.310): "dubnium",
    (0.122, 1.000, 0.780): "dysprosium",
    (0.702, 0.122, 0.831): "einsteinium",
    (0.000, 0.902, 0.459): "erbium",
    (0.380, 1.000, 0.780): "europium",
    (0.702, 0.122, 0.729): "fermium",
    (0.702, 1.000, 1.000): "fluorine",
    (0.259, 0.000, 0.400): "francium",
    (0.271, 1.000, 0.780): "gadolinium",
    (0.761, 0.561, 0.561): "gallium",
    (0.400, 0.561, 0.561): "germanium",
    (1.000, 0.820, 0.137): "gold",
    (0.302, 0.761, 1.000): "hafnium",
    (0.902, 0.000, 0.180): "hassium",
    (0.851, 1.000, 1.000): "helium",
    (0.000, 1.000, 0.612): "holmium",
    (0.900, 0.900, 0.900): "hydrogen",
    (0.651, 0.459, 0.451): "indium",
    (0.580, 0.000, 0.580): "iodine",
    (0.090, 0.329, 0.529): "iridium",
    (0.878, 0.400, 0.200): "iron",
    (0.361, 0.722, 0.820): "krypton",
    (0.439, 0.831, 1.000): "lanthanum",
    (0.780, 0.000, 0.400): "lawrencium",
    (0.341, 0.349, 0.380): "lead",
    (0.800, 0.502, 1.000): "lithium",
    (0.000, 0.671, 0.141): "lutetium",
    (0.541, 1.000, 0.000): "magnesium",
    (0.612, 0.478, 0.780): "manganese",
    (0.922, 0.000, 0.149): "meitnerium",
    (0.702, 0.051, 0.651): "mendelevium",
    (0.722, 0.722, 0.816): "mercury",
    (0.329, 0.710, 0.710): "molybdenum",
    (0.780, 1.000, 0.780): "neodymium",
    (0.702, 0.890, 0.961): "neon",
    (0.000, 0.502, 1.000): "neptunium",
    (0.314, 0.816, 0.314): "nickel",
    (0.451, 0.761, 0.788): "niobium",
    (0.200, 0.200, 1.000): "nitrogen",
    (0.741, 0.051, 0.529): "nobelium",
    (0.149, 0.400, 0.588): "osmium",
    (1.000, 0.300, 0.300): "oxygen",
    (0.000, 0.412, 0.522): "palladium",
    (1.000, 0.502, 0.000): "phosphorus",
    (0.816, 0.816, 0.878): "platinum",
    (0.000, 0.420, 1.000): "plutonium",
    (0.671, 0.361, 0.000): "polonium",
    (0.561, 0.251, 0.831): "potassium",
    (0.851, 1.000, 0.780): "praseodymium",
    (0.639, 1.000, 0.780): "promethium",
    (0.000, 0.631, 1.000): "protactinium",
    (0.000, 0.490, 0.000): "radium",
    (0.259, 0.510, 0.588): "radon",
    (0.149, 0.490, 0.671): "rhenium",
    (0.039, 0.490, 0.549): "rhodium",
    (0.439, 0.180, 0.690): "rubidium",
    (0.141, 0.561, 0.561): "ruthenium",
    (0.800, 0.000, 0.349): "rutherfordium",
    (0.561, 1.000, 0.780): "samarium",
    (0.902, 0.902, 0.902): "scandium",
    (0.851, 0.000, 0.271): "seaborgium",
    (1.000, 0.631, 0.000): "selenium",
    (0.941, 0.784, 0.627): "silicon",
    (0.753, 0.753, 0.753): "silver",
    (0.671, 0.361, 0.949): "sodium",
    (0.000, 1.000, 0.000): "strontium",
    (0.900, 0.775, 0.250): "sulfur",
    (0.302, 0.651, 1.000): "tantalum",
    (0.231, 0.620, 0.620): "technetium",
    (0.831, 0.478, 0.000): "tellurium",
    (0.188, 1.000, 0.780): "terbium",
    (0.651, 0.329, 0.302): "thallium",
    (0.000, 0.729, 1.000): "thorium",
    (0.000, 0.831, 0.322): "thulium",
    (0.400, 0.502, 0.502): "tin",
    (0.749, 0.761, 0.780): "titanium",
    (0.129, 0.580, 0.839): "tungsten",
    (0.000, 0.561, 1.000): "uranium",
    (0.651, 0.651, 0.671): "vanadium",
    (0.259, 0.620, 0.690): "xenon",
    (0.000, 0.749, 0.220): "ytterbium",
    (0.580, 1.000, 1.000): "yttrium",
    (0.490, 0.502, 0.690): "zinc",
    (0.580, 0.878, 0.878): "zirconium",
}

# Jsut combine them
combined_reverse_colors = {**reverse_simple_named_colors, **reverse_chemical_element_colors}

def get_color_name_from_rgb(rgb):
    """
    Returns the name of the color for a given RGB tuple.
    If the RGB tuple is not found, returns 'Unknown'.
    """
    return combined_reverse_colors.get(tuple(round(c, 3) for c in rgb), "Unknown")

def label_colors_with_names():
    """
    Labels residues or objects in PyMOL with their color names.
    """
    stored.atom_list = []
    cmd.iterate("all", "stored.atom_list.append([model, index, color])")

    for model, resi, color_index in stored.atom_list:
        # Get RGB tuple for this color index
        rgb = cmd.get_color_tuple(color_index)
        color_name = get_color_name_from_rgb(rgb)

        # Label the residue or object
        resi_selection = f"model {model} and index {resi}"
        cmd.label(resi_selection, f"'{color_name}'")

    print("Residues labeled with their color names.")

# Add the command to PyMOL
cmd.extend("show_color", label_colors_with_names)
