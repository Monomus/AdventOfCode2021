from os import spawnl

f = open('Input1.txt')

commands = f.read().splitlines()

ups = []
downs = []
forwards  = []

for command in commands:
    tuple = command.split(" ")
    match tuple[0]:
        case "forward":
            forwards.append(int(tuple[1]))
        case "up":
            ups.append(int(tuple[1]))
        case "down":
            downs.append(int(tuple[1]))

vertical = sum(downs)-sum(ups)

print(vertical * sum(forwards))
