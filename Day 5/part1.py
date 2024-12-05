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

for i, line in enumerate(updates):
    line: list[int]

    print(line)
    ruleBroken = False
    for x, char in enumerate(line):
        print(f"\n\nCHECKING: {char}\n\n")
        for rule in rules:
            if char == rule[0]:
                if rule[1] in line:
                    if x > line.index(rule[1]):
                        print(f"Char: {char} breaks rule: {rule}")
                        ruleBroken = True
            elif char == rule[1]:
                if rule[0] in line:
                    if x < line.index(rule[0]):
                        print(f"Char: {char} breaks rule: {rule}")
                        ruleBroken = True
        
    if ruleBroken:
        pass
    else:
        validLines.append(line)

for line in validLines:
    medianTotal += line[len(line) // 2]

print(f"Total Median: {medianTotal}")