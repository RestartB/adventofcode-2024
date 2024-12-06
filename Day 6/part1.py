lines: list[list[str]] = []
totalPlaces = 0

# Read file
with open("input.txt", "r") as f:
    linesRaw = f.readlines()

    for line in linesRaw:
        lines.append(list(line.rstrip("\n")))

try:
    while True:
        # Calculate movement
        for i, line in enumerate(lines):
            # Moving up
            if "^" in line:
                print("Moving up")
                arrowPos = line.index("^")

                if i == 0:
                    print("Guard has left")
                    line[arrowPos] = "X"

                    for line in lines:
                        print("".join(line))
                        totalPlaces += line.count("X")

                    print(totalPlaces)
                    exit()
                
                if lines[i - 1][arrowPos] == "#":
                    print("Hit a wall")
                    line[arrowPos] = ">"
                else:
                    print("Moved up")
                    line[arrowPos] = "X"
                    lines[i - 1][arrowPos] = "^"
            elif ">" in line:
                print("Moving right")
                arrowPos = line.index(">")

                if lines[i][arrowPos + 1] == "#":
                    print("Hit a wall")
                    line[arrowPos] = "v"
                else:
                    print("Moved right")
                    line[arrowPos] = "X"
                    lines[i][arrowPos + 1] = ">"
            elif "v" in line:
                print("Moving down")
                arrowPos = line.index("v")

                if lines[i + 1][arrowPos] == "#":
                    print("Hit a wall")
                    line[arrowPos] = "<"
                else:
                    print("Moved down")
                    line[arrowPos] = "X"
                    lines[i + 1][arrowPos] = "v"
            elif "<" in line:
                print("Moving left")
                arrowPos = line.index("<")

                if arrowPos == 0:
                    print("Guard has left")
                    line[arrowPos] = "X"

                    for line in lines:
                        print("".join(line))
                        totalPlaces += line.count("X")

                    print(totalPlaces)
                    exit()

                if lines[i][arrowPos - 1] == "#":
                    print("Hit a wall")
                    line[arrowPos] = "^"
                else:
                    print("Moved left")
                    line[arrowPos] = "X"
                    lines[i][arrowPos - 1] = "<"
except IndexError:
    print("Guard has left - index error")
    
    for line in lines:
        if ">" in line:
            line[line.index("v")] = "X"
        elif "v" in line:
            line[line.index("v")] = "X"
        
    for line in lines:
        totalPlaces += line.count("X")

print(totalPlaces)
exit()