import re

validMul = []
mulTotal = 0

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    # Remove trailing newline
    line = line.rstrip("\n")

    # Get all valid muls
    lineMatches = re.findall("mul\([0-9]?[0-9]?[0-9]\,[0-9]?[0-9]?[0-9]\)", line)
    
    for match in lineMatches:
        validMul.append(match)

# Calculate muls
for mul in validMul:
    mul: str
    mul = mul.replace("mul(", "").rstrip(")").split(",")

    mul[0] = int(mul[0])
    mul[1] = int(mul[1])

    mulTotal += mul[0] * mul[1]

print(f"Total: {mulTotal}")