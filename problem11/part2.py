with open('problem11_input.txt') as file:
    seats = file.read().splitlines()


def check_seats_in_direction(x, y, x_change, y_change, seats):

    i = 1
    current_x = x + (x_change * i)
    current_y = y + (y_change * i)

    while current_x in range(len(seats[y])) and current_y in range(len(seats)):
        current_seat = seats[current_y][current_x]
        if current_seat == '#':
            return 1
        elif current_seat == 'L':
            return 0

        i += 1
        current_x = x + (x_change * i)
        current_y = y + (y_change * i)

    return 0

def check_adjacent_seats(x, y, seats):
    count = 0

    count += check_seats_in_direction(x, y, 1, 0, seats) #RIGHT
    count += check_seats_in_direction(x, y, 1, 1, seats) #UP RIGHT
    count += check_seats_in_direction(x, y, 0, 1, seats) #UP
    count += check_seats_in_direction(x, y, -1, 1, seats) #UP LEFT
    count += check_seats_in_direction(x, y, -1, 0, seats) #LEFT
    count += check_seats_in_direction(x, y, -1, -1, seats) #DOWN LEFT
    count += check_seats_in_direction(x, y, 0, -1, seats) #DOWN
    count += check_seats_in_direction(x, y, 1, -1, seats) #DOWN RIGHT

    return count

def fill_seats(seats):
    new_seats = seats.copy()

    for y in range(0, len(seats)):
        for x in range(0, len(seats[y])):
            current_seat = seats[y][x]

            if current_seat == '#':
                if (check_adjacent_seats(x, y, seats) >= 5):
                    new_seats[y] = new_seats[y][:x] + 'L' + new_seats[y][x + 1:]

            elif current_seat == 'L':
                if (check_adjacent_seats(x, y, seats) == 0):
                    new_seats[y] = new_seats[y][:x] + '#' + new_seats[y][x + 1:]

    return new_seats

while True:

    new_seats = fill_seats(seats)

    if (seats == new_seats):
        break

    seats = new_seats

count = 0

for y in range(0, len(seats)):
    for x in range(0, len(seats[y])):
        if seats[y][x] == '#':
            count += 1

print(count)


