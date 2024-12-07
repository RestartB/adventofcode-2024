from itertools import product

lines = []
totalResults = 0

# Read file
with open("input.txt", "r") as f:
    linesRaw = f.readlines()

    for line in linesRaw:
        lineSplit = line.rstrip("\n").split(": ")

        lines.append([int(lineSplit[0]), [int(part) for part in lineSplit[1].split(" ")]])

# Try all combos of + and *
for line in lines:
    print(line)
    for combo in product(["+", "*"], repeat=(len(line[1]) - 1)):
        total = line[1][0]
        
        for i, operator in enumerate(combo):
            if operator == "+":
                total += line[1][i + 1]
            else:
                total *= line[1][i + 1]
        
        if total == line[0]:
            totalResults += total

            break

print(totalResults)