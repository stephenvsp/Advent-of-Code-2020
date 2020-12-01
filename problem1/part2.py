with open('problem1_input.txt') as file:
    inputs = file.readlines()

inputs = [int(i.strip()) for i in inputs]

target = 2020

for i in range(0, len(inputs) - 2):
    for j in range(1, len(inputs) - 1):
        for k in range(2, len(inputs)):
            num_one = inputs[i]
            num_two = inputs[j]
            num_three = inputs[k]
            if num_one + num_two + num_three == target:
                print(num_one * num_two * num_three)