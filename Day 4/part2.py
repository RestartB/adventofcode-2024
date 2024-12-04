import re

linesClean = []
foundX = 0

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line: str
        # Remove trailing newline
        linesClean.append(line.rstrip("\n"))

for i, line in enumerate(linesClean):
    if i <= len(linesClean) - 3:
        for x in range(len(line)):
            if x >= len(line) - 2:
                continue
            else:
                string = f"{linesClean[i][x]}{linesClean[i][x + 2]}{linesClean[i + 1][x + 1]}{linesClean[i + 2][x]}{linesClean[i + 2][x + 2]}"
                
                if string == "MMASS" or string == "SSAMM" or string == "MSAMS" or string == "SMASM":
                    foundX += 1

print(f"Total X Amount: {foundX}")