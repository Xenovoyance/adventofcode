input = "input.txt"

def main():
    fully_contained = 0
    partially_contained = 0
    lines = 0
    with open(input, "r") as f:
        for line in f.readlines():
            lines += 1
            pair = line.strip().split(",")

            tv = int(pair[0].split("-")[0])
            th = int(pair[0].split("-")[1])
            bv = int(pair[1].split("-")[0])
            bh = int(pair[1].split("-")[1])

            if (tv <= bv and th >= bh) or (tv >= bv and th <= bh): fully_contained += 1
            if th < bv or tv > bh: partially_contained += 1
    
    print("P1: " + str(fully_contained))
    print("P2: " + str(lines - partially_contained))

main()
