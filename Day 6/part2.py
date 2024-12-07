lines: list[list[str]] = []
loops = []

# Read file
with open("input.txt", "r") as f:
    linesRaw = f.readlines()

    for line in linesRaw:
        lines.append(list(line.rstrip("\n")))

def simulation(lines):
    states = []

    while True:
        # Calculate movement
        for i, line in enumerate(lines):
            # Moving up
            if "^" in line:
                # print("Moving up")
                arrowPos = line.index("^")

                if i == 0:
                    return False
                
                if lines[i - 1][arrowPos] == "#":
                    # print("Hit a wall")
                    line[arrowPos] = ">"

                    if (i, arrowPos, '>') in states:
                        return True
                    else:
                        states.append((i, arrowPos, '>'))
                else:
                    # print("Moved up")
                    line[arrowPos] = "X"
                    lines[i - 1][arrowPos] = "^"
                    
                    if (i - 1, arrowPos, '^') in states:
                        return True
                    else:
                        states.append((i - 1, arrowPos, '^'))
            elif ">" in line:
                # print("Moving right")
                arrowPos = line.index(">")

                if arrowPos == len(line) - 1:
                    return False

                if lines[i][arrowPos + 1] == "#":
                    # print("Hit a wall")
                    line[arrowPos] = "v"

                    if (i, arrowPos, 'v') in states:
                        return True
                    else:
                        states.append((i, arrowPos, 'v'))
                else:
                    # print("Moved right")
                    line[arrowPos] = "X"
                    lines[i][arrowPos + 1] = ">"

                    if (i, arrowPos + 1, '>') in states:
                        return True
                    else:
                        states.append((i, arrowPos + 1, '>'))
            elif "v" in line:
                # print("Moving down")
                arrowPos = line.index("v")

                if i == len(lines) - 1:
                    return False

                if lines[i + 1][arrowPos] == "#":
                    # print("Hit a wall")
                    line[arrowPos] = "<"

                    if (i, arrowPos, '<') in states:
                        return True
                    else:
                        states.append((i, arrowPos, '<'))
                else:
                    # print("Moved down")
                    line[arrowPos] = "X"
                    lines[i + 1][arrowPos] = "v"

                    if (i + 1, arrowPos, 'v') in states:
                        return True
                    else:
                        states.append((i + 1, arrowPos, 'v'))
            elif "<" in line:
                # print("Moving left")
                arrowPos = line.index("<")

                if arrowPos == 0:
                    return False

                if lines[i][arrowPos - 1] == "#":
                    # print("Hit a wall")
                    line[arrowPos] = "^"

                    if (i, arrowPos, '^') in states:
                        return True
                    else:
                        states.append((i, arrowPos, '^'))
                else:
                    # print("Moved left")
                    line[arrowPos] = "X"
                    lines[i][arrowPos - 1] = "<"

                    if (i - 1, arrowPos, '<') in states:
                        return True
                    else:
                        states.append((i - 1, arrowPos, '<'))

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == ".":
            temp = [line[:] for line in lines]
            temp[y][x] = '#'
            res = simulation(temp)
            # print(res)
            print("\n".join(["".join(x) for x in temp]))
            
            if res:
                loops.append(temp)

print()

print(f"Loops: {len(loops)}")

for loop in loops:
    for line in loop:
        pass#print("".join(line))

    #print()