

cycles = 0
X = 1
isFirst = True
sgnl_strngth = []

ls = []

with open("./day_10_sample_input.txt", 'r+') as inputFile:
    for line in inputFile:
        try:
            command, value = line[:-1].split(" ")
        except:
            command = line[:-1].split(" ")[0]

        if command == "noop":
            cycles += 1
        elif command == "addx":
            cycles += 2
            X += int(value)
        

        ls.append([line[:-1], cycles, X  ])
        print(line[:-1], cycles, X)

currentCycle = 0

signal = 1
for index, cycle in enumerate(ls):
    currentCycle = cycle[1]
    if currentCycle <= 220:
        print(signal)
        signal += cycle[2]

print(signal)  
