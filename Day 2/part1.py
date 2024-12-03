gradualLines = []
safeLines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

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
        pass
    elif not(increasing or decreasing):
        pass
    else:
        gradualLines.append(line)

for line in gradualLines:
    i = -1
    safe = True

    for value in line:
        i += 1
        
        if i == 0:
            pass
        else:
            first = int(line[i])
            last = int(line[i - 1])

            print(first, last)

            if abs(first - last) >= 1 and abs(first - last) <= 3:
                pass
            else:
                safe = False
    
    if safe:
        safeLines.append(line)

print(len(safeLines))