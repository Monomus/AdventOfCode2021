from os import spawnl

f = open('Input1.txt')

depths = f.read().splitlines()

olddepth = 0
counter = 0
for depth in depths:
    if(int(depth) > olddepth):
        counter += 1
    olddepth = int(depth)

#Correction for first beeing 0
print(counter-1)
    