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
    group_size = len(group)
    current_group = ''.join(group)

    frequency_map = {}

    for c in current_group:
        if c in frequency_map:
            frequency_map[c] += 1
        else:
            frequency_map[c] = 1

    total_for_group = 0


    for key in frequency_map.values():
        if key == group_size:
            total_for_group += 1
            
    total += total_for_group

print(total)