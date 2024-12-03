import re

enabledLines = []
validMul = []
mulTotal = 0
enabled = True

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    # Remove trailing newline
    line = line.rstrip("\n")

    # Split line by don't() and do()
    parts = re.split(r"(don't\(\)|do\(\))", line)

    # Work through parts
    for part in parts:
        # do() - enable
        if part == "do()":
            enabled = True
        # don't() - disable
        elif part == "don't()":
            enabled = False
        # Add part if enabled
        elif enabled:
            enabledLines.append(part)

# Get all valid muls
for line in enabledLines:
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