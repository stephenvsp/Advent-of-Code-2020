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

    count = password.count(character)

    if count >= lower_bound and count <= upper_bound:
        total_count += 1

print(total_count)