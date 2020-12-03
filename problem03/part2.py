from functools import reduce

with open('problem3_input.txt') as file:
    inputs = file.readlines()

slopes = [i.strip() for i in inputs]


def trees_ran_into(x, y, slopes):
    count = 0
    line_length = len(slopes[0])

    curr_x = 0
    curr_y = 0

    while curr_y < len(slopes):
        if slopes[curr_y][curr_x % line_length] == '#':
            count += 1
        
        curr_x += x
        curr_y += y

    return count

trees = []

trees.append(trees_ran_into(1, 1, slopes))
trees.append(trees_ran_into(3, 1, slopes))
trees.append(trees_ran_into(5, 1, slopes))
trees.append(trees_ran_into(7, 1, slopes))
trees.append(trees_ran_into(1, 2, slopes))

answer = reduce((lambda x, y: x * y), trees)

print(answer)