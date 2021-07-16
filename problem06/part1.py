with open('problem6_input.txt') as file:
    inputs = file.readlines()

inputs = [i.strip() for i in inputs]

groups = []
current_group = []

for group in inputs:
    if group == '':
        groups.append(current_group)
        current_group = []

    else:
        current_group.append(group)

groups.append(current_group)

total = 0

for group in groups:
    current_group = ''.join(group)
    unique_nums = ''.join(set(current_group))

    total += len(unique_nums)

print(total)