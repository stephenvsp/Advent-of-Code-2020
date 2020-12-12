with open('problem12_input.txt') as file:
    instructions = file.read().splitlines()

x = 0
y = 0
way_x = 10
way_y = 1
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
    

def move_waypoint(x, y, direction, value):
    if direction == 0:
        x += value
    elif direction == 1:
        y -= value
    elif direction == 2:
        x -= value
    else:
        y += value

    return x, y

def move_boat(x, y, way_x, way_y, value):
    x += way_x * value
    y += way_y * value

    return x, y

def turn(x, y, direction, value):
    if direction == 'L':
        if value == 90:
            return -y, x

        elif value == 180:
            return -x, -y

        elif value == 270:
            return y, -x

        else: 
            return x, y

    elif direction == 'R':
        if value == 90:
            return y, -x
        
        elif value == 180:
            return -x, -y

        elif value == 270:
            return -y, x

        else:
            return x, y

for i in instructions:

    direction = i[0]
    value = int(i[1:])

    if direction == 'R' or direction == 'L':
        way_x, way_y = turn(way_x, way_y, direction, value)
    elif direction == 'F':
        x, y = move_boat(x, y, way_x, way_y, value)
    else:
        way_x, way_y = move_waypoint(way_x, way_y, direction_to_int(direction), value)

print(abs(x) + abs(y))

