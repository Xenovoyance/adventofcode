input = "input.txt"
# I cut out the stacks from input and created them directly here instead. 
# So input contains only move orders

real_p1 = { 1: ['B','Z','T'],
    2: ['V','H','T','D','N'],
    3: ['B','F','M','D'],
    4: ['T','J','G','W','V','Q','L'],
    5: ['W','D','G','P','V','F','Q','M'],
    6: ['V','Z','Q','G','H','F','S'],
    7: ['Z','S','N','R','L','T','C','W'],
    8: ['Z','H','W','D','J','N','R','M'],
    9: ['M','Q','L','F','D','S']
}

real_p2 = { 1: ['B','Z','T'],
    2: ['V','H','T','D','N'],
    3: ['B','F','M','D'],
    4: ['T','J','G','W','V','Q','L'],
    5: ['W','D','G','P','V','F','Q','M'],
    6: ['V','Z','Q','G','H','F','S'],
    7: ['Z','S','N','R','L','T','C','W'],
    8: ['Z','H','W','D','J','N','R','M'],
    9: ['M','Q','L','F','D','S']
}

def move_9000 (s_amount, s_from, s_to):
    for i in range(s_amount): real_p1[s_to].append(real_p1[s_from].pop())

def move_9001 (s_amount, s_from, s_to):
    real_p2[s_to].extend(real_p2[s_from][-s_amount:])
    real_p2[s_from] = real_p2[s_from][:-s_amount]

def main():
    with open(input, "r") as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            move_9000(int(line[1]), int(line[3]), int(line[5]))
            move_9001(int(line[1]), int(line[3]), int(line[5]))

main()
print(real_p1)
print(real_p2)
