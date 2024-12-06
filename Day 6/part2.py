lines: list[list[str]] = []
loops = []

# Read file
with open("input.txt", "r") as f:
    linesRaw = f.readlines()

    for line in linesRaw:
        lines.append(list(line.rstrip("\n")))

def simulation(lines):
    try:
        states = []
        looping = False

        while True:
            # Calculate movement
            for i, line in enumerate(lines):
                # Moving up
                if "^" in line:
                    print("Moving up")
                    arrowPos = line.index("^")

                    if i == 0:
                        looping = False
                        raise IndexError
                    
                    if lines[i - 1][arrowPos] == "#":
                        print("Hit a wall")
                        line[arrowPos] = ">"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                    else:
                        print("Moved up")
                        line[arrowPos] = "X"
                        lines[i - 1][arrowPos] = "^"
                        
                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                elif ">" in line:
                    print("Moving right")
                    arrowPos = line.index(">")

                    if lines[i][arrowPos + 1] == "#":
                        print("Hit a wall")
                        line[arrowPos] = "v"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                    else:
                        print("Moved right")
                        line[arrowPos] = "X"
                        lines[i][arrowPos + 1] = ">"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                elif "v" in line:
                    print("Moving down")
                    arrowPos = line.index("v")

                    if lines[i + 1][arrowPos] == "#":
                        print("Hit a wall")
                        line[arrowPos] = "<"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                    else:
                        print("Moved down")
                        line[arrowPos] = "X"
                        lines[i + 1][arrowPos] = "v"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                elif "<" in line:
                    print("Moving left")
                    arrowPos = line.index("<")

                    if arrowPos == 0:
                        looping = False
                        raise IndexError

                    if lines[i][arrowPos - 1] == "#":
                        print("Hit a wall")
                        line[arrowPos] = "^"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
                    else:
                        print("Moved left")
                        line[arrowPos] = "X"
                        lines[i][arrowPos - 1] = "<"

                        if lines in states:
                            looping = True
                            raise IndexError
                        else:
                            states.append(lines)
    except IndexError:
        print("Guard has left")

        if looping:
            print("Looping")
            return True
        else:
            return False

for lineToTry in lines:
    for char in lineToTry:
        if char == ".":
            charReplaced = lineToTry.index(char)
            lineToTry[lineToTry.index(char)] = "#"
            
            if simulation(lines):
                loops.append(lines)
            
            lineToTry[charReplaced] = "." # Reset the place

print()

print(f"Loops: {len(loops)}")

for loop in loops:
    for line in loop:
        print("".join(line))

    print()