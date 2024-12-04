linesClean = []
horizontalXmas = 0
verticalXmas = 0
diagonalXmas = 0

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line: str
        # Remove trailing newline
        linesClean.append(line.rstrip("\n"))

for i, line in enumerate(linesClean):
    # Find horizontal xmas
    horizontalXmas += line.count("XMAS") + line.count("SAMX")

    # Find vertical xmas
    for x in range(len(line)):
        try:
            string = f"{linesClean[i][x]}{linesClean[i + 1][x]}{linesClean[i + 2][x]}{linesClean[i + 3][x]}"
            verticalXmas += (1 if string == "XMAS" or string == "SAMX" else 0)
        except IndexError:
            pass

    # Find diagonal forward xmas
    for x in range(len(line)):
        try:
            string = f"{linesClean[i][x]}{linesClean[i + 1][x + 1]}{linesClean[i + 2][x + 2]}{linesClean[i + 3][x + 3]}"
            diagonalXmas += (1 if string == "XMAS" or string == "SAMX" else 0)
        except IndexError:
            pass
    
    # Find diagonal backward xmas
    for x in range(len(line)):
        try:
            if x >= 3:
                string = f"{linesClean[i][x]}{linesClean[i + 1][x - 1]}{linesClean[i + 2][x - 2]}{linesClean[i + 3][x - 3]}"
                diagonalXmas += (1 if string == "XMAS" or string == "SAMX" else 0)
            else: pass
        except IndexError:
            pass

print(f"Horizontal Xmas Amount: {horizontalXmas}")
print(f"Vertical Xmas Amount: {verticalXmas}")
print(f"Diagonal Xmas Amount: {diagonalXmas}")

print(f"Total Xmas Amount: {horizontalXmas + verticalXmas + diagonalXmas}")