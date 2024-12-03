safeLines = []

# Line check function
def checkLine(line: list):
    x = -1
    safe = True

    increasing = False
    decreasing = False
    
    for x in range(len(line)):
        if x == 0:
            continue

        print(f"Checking {line[x]} and {line[x - 1]}")
        if int(line[x]) > int(line[x - 1]):
            increasing = True
        elif int(line[x]) < int(line[x - 1]):
            decreasing = True
    
    if increasing and decreasing:
        print(f"Line is increasing and decreasing {line}")
        safe = False
        return safe
    
    i = -1
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
            # Line is unsafe
            else:
                safe = False
                break
    
    return safe

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Check if line is gradual
for line in lines:
    formattedLine = []
    line = line.split(" ")

    for value in line:
        formattedLine.append(int(value.rstrip("\n")))
    
    line = formattedLine

    if checkLine(line):
        safeLines.append(line)
    else:
        for i in range(len(line)):
            testList = line.copy()

            testList.pop(i)

            if checkLine(testList):
                safeLines.append(line)
                break

print(len(safeLines))