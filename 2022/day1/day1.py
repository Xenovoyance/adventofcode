input = "input.txt"
elfs = []

with open(input, "r") as f:
    calories = 0
    for line in f.readlines():
        if line.strip() == '':
            elfs.append(calories)
            calories = 0
        else:
            calories = calories + int(line.strip())
    elfs.append(calories)

print("Part 1: " + str(max(elfs)))

first = max(elfs)
elfs.remove(max(elfs))
second = max(elfs)
elfs.remove(max(elfs))
third = max(elfs)

print("Part 2: " + str(first + second + third))
