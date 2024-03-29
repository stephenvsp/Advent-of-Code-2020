with open('problem2_input.txt') as file:
    inputs = file.readlines()


total_count = 0
for i in inputs:
    split = i.split(' ')

    bounds = split[0].split('-')
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])

    character = split[1][0]

    password = split[2]

    if (password[lower_bound - 1] == character) ^ (password[upper_bound - 1] == character):
        total_count += 1

print(total_count)