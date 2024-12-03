leftSide = []
rightSide = []
differences = []

with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    lineSplit = line.split("   ")
    leftSide.append(int(lineSplit[0]))
    rightSide.append(int(lineSplit[1]))

leftSide.sort()
rightSide.sort()

for i in range(len(leftSide)):
    differences.append(abs(leftSide[i] - rightSide[i]))

print(f"Location ID: {sum(differences)}")