with open('problem1_input.txt') as file:
    inputs = file.readlines()

inputs = [int(i.strip()) for i in inputs]

target = 2020

def loop(inputs):
    for i in range(0, len(inputs) - 2):
        for j in range(i + 1, len(inputs) - 1):
            for k in range(j + 1, len(inputs)):
                num_one = inputs[i]
                num_two = inputs[j]
                num_three = inputs[k]
                if num_one + num_two + num_three == target:
                    return num_one * num_two * num_three

print(loop(inputs))