with open('problem14_input.txt') as file:
    inputs = file.read().splitlines()

memory = {}

mask = ''

def apply_mask(mask, value):
    value = bin(value)[2:]
    value = value.zfill(len(mask))

    value = [char for char in value]

    for i in range(0, len(mask)):
        if mask[i] == 'X':
            value[i] = 'X'
        elif mask[i] == '1':
            value[i] = '1'

    return ''.join(value)

def generate_indicies(address):
    address = [char for char in address]

    address.reverse()

    x_positions = []

    for i in range(0, len(address)):
        if address[i] == 'X':
            x_positions.append(i)

    num_xes = len(x_positions)

    addresses = [address[:] for i in range(2 ** num_xes)]

    for i in range(0, num_xes):
        for j in range(0, len(addresses)):
            value = (j // (2 ** i)) % 2
            position = x_positions[i]
            addresses[j][position] = str(value)

    for address in addresses:
        address.reverse()

    addresses = [''.join(address) for address in addresses]

    addresses = [int(address, 2) for address in addresses]
    
    return addresses

for i in inputs:
    if 'mask' in i:
        mask = i.split(' ')[-1]
    else:
        split = i.split(' ')
        index = int(split[0][4:-1])
        value = int(split[-1])
        
        floating_index = apply_mask(mask, index)

        indicies = generate_indicies(floating_index)

        for i in indicies:
            memory[i] = value

total = 0

for value in memory.values():
    
    total += value

print(total)