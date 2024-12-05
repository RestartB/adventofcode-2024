import time

rules = []
updates = []
validLines = []
medianTotal = 0

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()
    rulesSection = True

    for fileLine in lines:
        fileLine: str
        
        if fileLine.rstrip("\n") == "":
            rulesSection = False
            continue
        else:
            if rulesSection:
                rules.append(list(map(int, fileLine.rstrip("\n").split("|"))))
            else:
                updates.append(list(map(int, fileLine.rstrip("\n").split(","))))

print("Rules: ", rules)
print("Total lines: ", len(updates))

for i, line in enumerate(updates):
    line: list[int]

    ruleBroken = False
    for x, page in enumerate(line):
        for rule in rules:
            if page == rule[0]:
                if rule[1] in line:
                    if x > line.index(rule[1]):
                        ruleBroken = True
            elif page == rule[1]:
                if rule[0] in line:
                    if x < line.index(rule[0]):
                        ruleBroken = True
        
    if ruleBroken:
        pass
    else:
        validLines.append(line)
    
for line in validLines:
    updates.remove(line)

print(f"Broken lines: {len(updates)}")

time.sleep(5)

# Fix broken lines
for i, line in enumerate(updates):
    line: list[int]

    print(line)
    for x, page in enumerate(line):
        ruleBroken = True
        
        if ruleBroken:
            for rule in rules:
                if page in rule:
                    for y, pageAfterCut in enumerate(line[x:]):
                        if pageAfterCut in rule:
                            if page == rule[0]:
                                if x > line.index(pageAfterCut):
                                    line.insert(x + 1, pageAfterCut)
                            else:
                                if x < line.index(pageAfterCut):
                                    line.insert(x, pageAfterCut)

for line in updates:
    medianTotal += line[len(line) // 2]

print(updates)
print(f"Total Median: {medianTotal}")