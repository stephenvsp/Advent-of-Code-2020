import cmath

with open('problem12_input.txt') as file:
    instructions = file.read().splitlines()

ship = complex(0, 0)
waypoint = complex(10, 1)

for i in instructions:

    action, magnitude = i[:1], int(i[1:])

    if action == 'N':
        waypoint += complex(0, magnitude)
    elif action == 'S':
        waypoint += complex(0, -magnitude)
    elif action == 'E':
        waypoint += complex(magnitude, 0)
    elif action == 'W':
        waypoint += complex(-magnitude, 0)
    elif action == 'F':
        ship += waypoint * magnitude
    elif action == 'R':
        waypoint *= complex(0, -1)**(magnitude // 90)
    elif action == 'L':
        waypoint *= complex(0, 1)**(magnitude // 90)

print(ship)

