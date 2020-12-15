with open('problem14_input.txt') as file:
    inputs = file.read().splitlines()

memory = {}

mask = ''

def apply_mask(mask, value):
    value = bin(value)[2:]
    value = value.zfill(len(mask))

    value = [char for char in value]

    for i in range(0, len(mask)):
        if mask[i] != 'X':
            value[i] = mask[i]

    return ''.join(value)

for i in inputs:
    if 'mask' in i:
        mask = i.split(' ')[-1]
    else:
        split = i.split(' ')
        index = int(split[0][4:-1])
        value = int(split[-1])
        
        memory[index] = apply_mask(mask, value)

total = 0

for value in memory.values():
    total += int(value, 2)

print(total)
