# Treasure_map_python
# Treasure Hunt Game

Ever thought about hiding a treasure on a map? This little Python project lets you do just that in a fun and interactive way!

## What Is It?

This project is a simple script that creates a 3x3 grid filled with checkmarks ("☑️"). It then asks you to choose a spot on the grid to hide your treasure. Once you enter your chosen position (like "23" for column 2, row 3), the program updates the grid by placing a treasure emoji ("🪙") at that spot.

## How It Works

- **The Grid:**  
  The grid is built using three lists—each representing a row filled with checkmarks. These rows are then combined into one larger list to form the map.

- **User Input:**  
  The program prints the grid and then asks you where you’d like to place your treasure. You provide a two-digit number where the first digit is the column and the second is the row.

- **Placing the Treasure:**  
  The script converts your input into indices (taking into account that Python starts counting at 0) and replaces the appropriate checkmark with a treasure emoji.

- **Displaying the Result:**  
  Finally, the updated grid is printed so you can see exactly where your treasure has been hidden.


   git clone https://github.com/your_username/treasure-hunt.git
