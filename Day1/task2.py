from os import spawnl

f = open('Input1.txt')

depths = f.read().splitlines()

tuples = zip(depths,depths[1:],depths[2:])

depths = []

for tuple in list(tuples):
    depths.append(sum(map(int, list(tuple))))
    
olddepth = 0
counter = 0
print(len(depths))
for depth in depths:
    if(depth > olddepth):
        counter += 1
    olddepth = depth

#Correction for first beeing 0
print(counter-1)