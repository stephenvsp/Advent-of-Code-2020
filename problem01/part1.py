with open('problem1_input.txt') as file:
    inputs = file.readlines()

inputs = [int(i.strip()) for i in inputs]

complement_map = {}
target = 2020

for i in inputs:
    if i in complement_map:
        complement = 2020 - i
        print(i * complement)
    else:
        complement_map[2020 - i] = i