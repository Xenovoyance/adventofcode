
input = "input.txt"

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1():
    partone = 0
    with open(input, "r") as f:
        for line in f.readlines():           
            line = line.strip()
            rugsack = [line[:int(len(line) / 2)],line[int(len(line) / 2):]]
            rugsack_intersection = list(set(rugsack[0]).intersection(rugsack[1]))

            if rugsack_intersection[0].islower(): partone += lowercase.index(rugsack_intersection[0]) + 1
            else: partone += uppercase.index(rugsack_intersection[0]) + 27

    return partone

def p2():
    parttwo = 0
    with open(input, "r") as f:
        i = 0
        rugsacks = []
        for rugsack in f.readlines():           
            rugsack = rugsack.strip()
            rugsacks.append(rugsack)

            if i > 1:
                rugsack_intersection = list(set(rugsacks[0]).intersection(set(rugsacks[1]).intersection(set(rugsacks[2]))))
                if rugsack_intersection[0].islower(): parttwo += lowercase.index(rugsack_intersection[0]) + 1
                else: parttwo += uppercase.index(rugsack_intersection[0]) + 27
                i = 0
                rugsacks.clear()
            else: 
                i += 1

    return parttwo

print( p1() )
print( p2() )
