import re
import copy


def dataParser():
    monkeys = []
    with open("./day_11_input.txt", 'r+') as inputFile:
        block = inputFile.read().split("\n\n")

        for monkey in block:
            monkey_data = monkey.split("\n")
            items = re.findall('[0-9][0-9]', monkey_data[1])
            items = [int(x) for x in items]
            operation = monkey_data[2][monkey_data[2].index("=") + 1:].strip()
            test = int(re.findall('\d+', monkey_data[3])[0])
            ifTrue = int(re.findall('[0-9]', monkey_data[4])[0])
            ifFalse = int(re.findall('[0-9]', monkey_data[5])[0])
            monkeys.append([items, operation, test, ifTrue, ifFalse])
    
    return monkeys

def worryCal(monkeys):
    print("monkeys -> "+str(monkeys))
    inspected_items = [0 for i in range(0, len(monkeys))]
    for i in range(0,20):
        for index in range(0, len(monkeys)):
            temp_monkeys = copy.deepcopy(monkeys)
            monkey = monkeys[index]
            for item in monkey[0]:
                inspected_items[index] += 1
                ifTrue = monkey[3]
                ifFalse = monkey[4]
                old = item
                new = eval(monkey[1])
                # new = new // 3

                if new % monkey[2] == 0:
                    temp_monkeys[ifTrue][0].append(new) 
                    temp_monkeys[index][0].remove(item)
                else:
                    temp_monkeys[ifFalse][0].append(new) 
                    temp_monkeys[index][0].remove(item)
            monkeys = temp_monkeys[:]
    print(inspected_items)
    return sorted(inspected_items)[-2:]
    
if __name__ == "__main__":
    monkeys = dataParser()
    inspected = worryCal(monkeys)
    mon_business = inspected[0] * inspected[1]
    print(mon_business)


