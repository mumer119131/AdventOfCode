input_ = open("input.txt", "r")

tail_mvmnts = 0

prev_mvmnt = ["s", 0]

log_str = ""
tail_positions = set()

tail_pos = [0,0]
for x in input_:

    mvmnt = x[:-1].split(" ")
    isAdjacant = False
    if (prev_mvmnt[0] in ["D", "U"] and int(prev_mvmnt[1]) == 1 and mvmnt[0] in ["L", "R"]) or (prev_mvmnt[0] in ["L", "R"] and int(prev_mvmnt[1]) == 1 and mvmnt[0] in ["U", "D"]):
        isAdjacant = True
            
    elif (prev_mvmnt[0] == "L" and mvmnt[0] == "R") or (prev_mvmnt[0] == "R" and mvmnt[0] == "L") or (prev_mvmnt[0] == "U" and mvmnt[0] == "D") or (prev_mvmnt[0] == "D" and mvmnt[0] == "U"):
        isAdjacant = True
    else:
        tail_mvmnts += int(mvmnt[1]) - 1
        print((tail_pos[1] + 1, int(mvmnt[1]) - 1))
        for i in range(tail_pos[1] + 1, int(mvmnt[1])):
            if mvmnt[0] == "U":
                tail_pos[1] += 1
            elif mvmnt[0] == "D":
                tail_pos[1] -= 1
            elif mvmnt[0] == "R":
                tail_pos[0] += 1
            elif mvmnt[0] == "L":
                tail_pos[0] -= 1
            print(i, tail_pos)
             
            tail_positions.add(tuple(tail_pos))
            log_str += f'{str(mvmnt)} {str(tail_pos)}\n'
    
    if isAdjacant:
        if int(mvmnt[1]) > 2:
            tail_mvmnts += int(mvmnt[1]) - 2
            for i in range(tail_pos[1], int(mvmnt[1]) - 1):
                if mvmnt[0] == "U":
                    tail_pos[1] += 1
                elif mvmnt[0] == "D":
                    tail_pos[1] -= 1
                elif mvmnt[0] == "R":
                    tail_pos[0] += 1
                elif mvmnt[0] == "L":
                    tail_pos[0] -= 1
                tail_positions.add(tuple(tail_pos))
                log_str += f'{str(mvmnt)} {str(tail_pos)}\n'

    # log_str += f'{tail_mvmnts} {str(mvmnt)} {str(prev_mvmnt)}  \n'
    prev_mvmnt = mvmnt



with open('output.txt', 'w+') as outFile:
    outFile.write(log_str)
print(tail_mvmnts)
print(len(tail_positions))