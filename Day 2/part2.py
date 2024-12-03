gradualLines = []
safeLines = []

# Line check function
def checkLine(line: list):
    i = -1
    safe = True
    unsafeValues = []

    # For each value in line
    for value in line:
        i += 1
        
        # Skip first value
        if i == 0:
            pass
        else:
            first = int(value)
            last = int(line[i - 1])

            # If difference is between 1 and 3, safe - pass
            if abs(first - last) >= 1 and abs(first - last) <= 3:
                pass
            # Line is unsafe - add unsafe value to list
            else:
                unsafeValues.append(value)
                safe = False
    
    return safe

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Check if line is gradual
for line in lines:
    line = line.split(" ")

    increasing = False
    decreasing = False

    for i in range(len(line)):
        if i == 0:
            continue

        if int(line[i]) > int(line[i - 1]):
            increasing = True
        elif int(line[i]) < int(line[i - 1]):
            decreasing = True
    
    if increasing and decreasing:
        for i in range(len(line)):
            testList = line.copy()

            testList.pop(i)

            if checkLine(testList):
                print(f"Increasing and decreasing - Line check success (removed {line[i]}) {line}")
                safeLines.append(line)
                break
            else:
                pass
    elif not(increasing or decreasing):
        pass
    else:
        if checkLine(line):
            print(f"Line check success {line}")
            safeLines.append(line)
        else:
            for i in range(len(line)):
                testList = line.copy()

                testList.pop(i)

                if checkLine(testList):
                    print(f"Remove 1 - Line check success (removed {line[i]}) {line}")
                    safeLines.append(line)
                    break
                else:
                    pass

print(len(safeLines))