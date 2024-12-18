import threading    
inputFile = "2024/day-17/python/" + ("sampleInput" if False else "input") + ".txt"
file = open(inputFile).readlines()
registerA = int(file[0].split(" ")[2])
registerB = int(file[1].split(" ")[2])
registerC = int(file[2].split(" ")[2])
program = file[4].split(" ")[1]
print(program)

combo = lambda o, r: o if o <=3 else r[o-4]

def run(program, A,B=0,C=0):
    instructionPointer = 0   
    output = ""
    p = program.split(",")
    fresh = True
    while(instructionPointer<len(p)):
        instruction = int(p[instructionPointer])
        operand = int(p[instructionPointer+1])
        match instruction:
            case 0: A =   int(A/(2 ** combo(operand, [A,B,C])))
            case 1: B ^= operand
            case 2: B = combo(operand, [A,B,C]) % 8
            case 3: instructionPointer = operand - 2 if A != 0 else instructionPointer
            case 4: B ^= C
            case 5: output+= ("" if fresh else ",") + (str(combo(operand, [A,B,C]) % 8)); fresh = False
            case 6: B = int(A/(2 ** combo(operand, [A,B,C])))
            case 7: C = int(A/(2 ** combo(operand, [A,B,C])))
        #if not fresh and output not in program:
        #    return "skipped"
        instructionPointer += 2
    return(output)
print(run(program, registerA),end="\n---\n")
step = 164278899142333 #35184372088831
output = ""
prev = 0
while (True or output != program):
    output = run(program, step)
    if output == program:
        print(step)
    testSub = "2,4,1,1,7,5"
    if output[:len(testSub)] == testSub:
        print(step, len(output), len(program), step-prev, output)
        prev = step
    step-=1
    #print(run(program, step) ,"|", program)
    #break
print(step)