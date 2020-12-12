with open('problem12_input.txt') as file:
    instructions = file.read().splitlines()

x = 0
y = 0
#E == 0, S == 1, W == 2, N == 3
facing = 0

def move(x, y, direction, value):
    if direction == 0 or direction == 'E':
        x += value
    elif direction == 1 or direction == 'S':
        y -= value
    elif direction == 2 or direction == 'W':
        x -= value
    elif direction == 3 or direction == 'N':
        y += value

    return x, y

for i in instructions:

    direction = i[0]
    value = int(i[1:])

    if direction == 'R':
        facing += (value / 90)
        facing %= 4
    elif direction == 'L':
        facing -= (value / 90)
        facing += 4
        facing %= 4
    elif direction == 'F':
        x, y = move(x, y, facing, value)
    else:
        x, y = move(x, y, direction, value)

print(abs(x) + abs(y))

