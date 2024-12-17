import threading
inputFile = "2024/day-17/python/" + ("sampleInput" if False else "input") + ".txt"
file = open(inputFile).readlines()
registerA = int(file[0].split(" ")[2])
registerB = int(file[1].split(" ")[2])
registerC = int(file[2].split(" ")[2])
registers = [registerA, registerB, registerC]
print(registers)
program = file[4].split(" ")[1]
print(program)
def combo(operand, registers):
    if operand in [0,1,2,3]:
        return operand
    if operand in [4,5,6]:
        return registers[operand-4]
def run(r, result):
    registers = r[:]
    instructionPointer = 0   
    output = ""
    p = program.split(",")
    while(instructionPointer<len(p)):
        instruction = int(p[instructionPointer])
        operand = int(p[instructionPointer+1])
        #print(instruction)
        match instruction:
            case 0:
                registers[0] =   int(registers[0]/(2 ** combo(operand, registers)))
            case 1:
                registers[1] ^= operand
            case 2:
                registers[1] = combo(operand, registers) % 8
            case 3:
                if registers[0] != 0:
                    instructionPointer = operand
                    continue
            case 4:
                registers[1] ^= registers[2]
            case 5:
                output+=(str(combo(operand, registers) % 8)) +","
            case 6:
                registers[1] = int(registers[0]/(2 ** combo(operand, registers)))
            case 7:
                registers[2] = int(registers[0]/(2 ** combo(operand, registers)))
        instructionPointer += 2
        if output[:-1] == program:
            result[0] = r[0]
    return(output[:-1])
print(run(registers, {}))
a = 0
intensity = 10000
result = {}
while (True):
    print(a)
    for i in range(intensity):
        copy = registers[:]
        copy[0] = a+i
        threading.Thread(target=run, args=(copy, result)).start()
        #print(a+i)
    registers[0] = a
    if len(result) >0:
        print(result[0])
        break
    a+=intensity

#pt 1 is working, pt 2 is kicking my butt