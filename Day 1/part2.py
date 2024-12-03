leftSide = []
rightSide = []
similarity = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    lineSplit = line.split("   ")
    leftSide.append(int(lineSplit[0]))
    rightSide.append(int(lineSplit[1]))

leftSide.sort()
rightSide.sort()

for value in leftSide:
    similarity += value * rightSide.count(value)

print(f"Similarity value: {similarity}")