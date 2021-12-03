from os import spawnl

f = open('Input1.txt')

commands = f.read().splitlines()

vertical = 0
horizontal = 0
aim = 0 

for command in commands:
    tuple = command.split(" ")
    match tuple[0]:
        case "forward":
            horizontal += int(tuple[1])
            vertical += int(tuple[1])*aim
        case "up":
            aim -= int(tuple[1])
        case "down":
            aim += int(tuple[1])

print(horizontal)
print(vertical)
print(horizontal*vertical)