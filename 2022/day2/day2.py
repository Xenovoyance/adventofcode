input = "input.txt"

def part_one():
    part_one = 0
    with open(input, "r") as f:
        for line in f.readlines():
            gameround = line.strip().split(" ")
            if (gameround[0] == "A"): gameround[0] = "X"
            if gameround[0] == "B": gameround[0] = "Y"
            if gameround[0] == "C": gameround[0] = "Z"
        
            if gameround[1] == "X": part_one += 1
            if gameround[1] == "Y": part_one += 2
            if gameround[1] == "Z": part_one += 3

            if gameround[0] == gameround[1]: part_one += 3 # round is draw
            if (gameround[1] == "X" and gameround[0] == "Z") or (gameround[1] == "Y" and gameround[0] == "X") or (gameround[1] == "Z" and gameround[0] == "Y"):
                part_one += 6
    return str(part_one)

def part_two():
    part_two = 0
    with open(input, "r") as f:
        for line in f.readlines():
            gameround = line.strip().split(" ")

            if gameround[0] == "A":
                if gameround[1] == "X":
                    part_two += 3 # opponent pick rock, I loose with scissor 0+3
                elif gameround[1] == "Y":
                    part_two += 4 # opponent pick rock, I also pick rock 1+3
                elif gameround[1] == "Z":
                    part_two += 8 # opponent pick rock, I win with paper 2+6
            elif gameround[0] == "B":
                if gameround[1] == "X":
                    part_two += 1 # opponent pick paper, I lose with rock 1+0
                elif gameround[1] == "Y":
                    part_two += 5 # opponent pick paper, I draw with paper 2+3
                elif gameround[1] == "Z":
                    part_two += 9 # opponent pick paper, I win with sciossor 3+6
            elif gameround[0] == "C":
                if gameround[1] == "X":
                    part_two += 2 # opponent pick scissor, I lose with paper 2+0
                elif gameround[1] == "Y":
                    part_two += 6 # opponent pick scissor, I draw with scissor 3+3
                elif gameround[1] == "Z":
                    part_two += 7 # opponent pick scissor, I win with rock 1+6
    return str(part_two)

print ( "Part 1: " + part_one())
print ( "Part 2: " + part_two())
