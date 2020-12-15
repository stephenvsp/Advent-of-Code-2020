with open('problem14_input.txt') as file:
    inputs = file.read().splitlines()

mask = ''

for i in inputs:
    if 'mask' in i:
        mask = i.split(' ')[-1]
        print(mask)
    else:
        split = i.split(' ')
        index = int(split[0][4:-1])
        value = int(split[-1])
        print(index, value)
