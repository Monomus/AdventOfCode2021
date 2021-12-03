from os import spawnl

f = open('Input1.txt')

numbers = f.read().splitlines()

numberList = list(map(list, numbers))
gamma = ["" for x in range(len(numberList[0]))]
epsilon = ["" for x in range(len(numberList[0]))]

for i in range(len(numberList[0])):
    rowcnt = 0
    for line in numberList:
        if(line[i] == '1'):
            rowcnt += 1
        else:
            rowcnt -= 1
    
    if(rowcnt >= 0):
        gamma[i] = '1'
        epsilon[i] = '0'
    else:
        gamma[i] = '0'
        epsilon[i] = '1'
    rowcnt = 0

gammaValue = int("".join(gamma),2)
epsilonValue = int("".join(epsilon),2)

print(gammaValue * epsilonValue)



