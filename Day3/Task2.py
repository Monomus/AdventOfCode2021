from os import spawnl

f = open('Input1.txt')

numbers = f.read().splitlines()

numberList = list(map(list, numbers))
ox = numberList.copy()
co2 = numberList.copy()
valueLength = len(numberList[0])

for i in range(valueLength):
    if(len(ox) > 1):
        oxcount = 0    
        for line in ox:
            if(line[i] == '1'):
                oxcount += 1
            else:
                oxcount -= 1
        if(oxcount >= 0):
            ox = list(filter(lambda x: x[i] == '1' , ox))
        else:
            ox = list(filter(lambda x: x[i] == '0' , ox))
        oxcount = 0

    if(len(co2) > 1):
        co2count = 0 
        for line in co2:
            if(line[i] == '1'):
                co2count += 1
            else:
                co2count -= 1
        if(co2count >= 0):
            co2 = list(filter(lambda x: x[i] == '0' , co2))
        else:
            co2 = list(filter(lambda x: x[i] == '1' , co2))
        co2count = 0 


oxValue = int("".join(ox[0]),2)
co2Value = int("".join(co2[0]),2)

print(oxValue * co2Value)










