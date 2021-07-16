with open('problem12_input.txt') as file:
    instructions = file.read().splitlines()

ship = complex(0, 0)
waypoint = complex(10, 1)

directions = {'N':(0, 1), 'S':(0, -1), 'E':(1,0), 'W':(-1, 0)}
rotation = {'R':(0, -1), 'L':(0, 1)}

for i in instructions:

    action, magnitude = i[:1], int(i[1:])

    if action in 'NSEW':
        vector = directions[action]
        waypoint += complex(vector[0] * magnitude, vector[1] * magnitude)
    elif action in 'RL':
        vector = rotation[action]
        waypoint *= complex(vector[0], vector[1])**(magnitude // 90)
    else:
        ship += waypoint * magnitude

print(ship.real + ship.imag)


