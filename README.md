# **`show_color` @ PyMOL**

## **Overview**

`show_color` labels atoms in PyMOL with their corresponding color names. This helps you identify colors directly in the visualization without guessing or manually checking RGB values.

---

## **Usage**

1. Load the script in PyMOL:
   ```python
   run show_color.py
   ```
2. Use the `show_color` command:
   ```python
   show_color
   ```
   - Labels residues or atoms with their current color names.

---

## **Features**

- Identifies common named colors (e.g., `red`, `cyan`) and chemical element-specific colors (e.g., `carbon`, `oxygen`).
- Automatically maps RGB values to color names.
- Simple and intuitive—just run and see!

---

## **Why Use It?**
No more asking, *"What is this color?"* Let the script handle it!

--- 

## **Customizing**

Want to add more colors? Update the dictionaries in the script:
```python
reverse_simple_named_colors = {
    (1.0, 0.0, 0.0): "red",
    ...
}
reverse_chemical_element_colors = {
    (1.0, 0.3, 0.3): "oxygen",
    ...
}
```

## **License**

This script is open-source and available under the MIT License.

<img src="assets/hem.png" alt="Example" width="600">