n = 10
# Open a file in write mode
with open("christmas_tree.txt", "w") as file:
    for i in range(0, n):
        # Create a line for the current row
        line = ""
        for j in range(1, n - i):
            line += " "  # Add spaces
        line += "*"  # Add the first star
        for k in range(0, i):
            line += "!"  # Add exclamation marks on the left
        for j in range(1, i):
            line += "!"  # Add exclamation marks on the right
        if i > 0:
            line += "*"  # Add the last star
        line += "\n"  # Move to the next line
        file.write(line)  # Write the line to the file

print("Pattern has been written to 'christmas_tree.txt'.")







