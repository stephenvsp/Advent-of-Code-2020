with open('problem12_input.txt') as file:
    instructions = file.read().splitlines()

x = 0
y = 0
#E == 0, S == 1, W == 2, N == 3
facing = 0

def direction_to_int(direction):
    if direction == 'E':
        return 0
    elif direction == 'S':
        return 1
    elif direction == 'W':
        return 2
    else:
        return 3
    

def move(x, y, direction, value):
    if direction == 0:
        x += value
    elif direction == 1:
        y -= value
    elif direction == 2:
        x -= value
    else:
        y += value

    return x, y

def turn(facing, value, direction):
    facing += (value / 90) * direction
    facing %= 4
    return facing

for i in instructions:

    direction = i[0]
    value = int(i[1:])

    if direction == 'R':
        facing = turn(facing, value, 1)
    elif direction == 'L':
        facing = turn(facing, value, -1)
    elif direction == 'F':
        x, y = move(x, y, facing, value)
    else:
        x, y = move(x, y, direction_to_int(direction), value)

print(abs(x) + abs(y))

