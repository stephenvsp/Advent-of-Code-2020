with open('problem5_input.txt') as file:
    inputs = file.readlines()

boarding_passes = [i.strip() for i in inputs]

highest = 0

for boarding_pass in boarding_passes:

    boarding_pass = boarding_pass.replace('B','1')
    boarding_pass = boarding_pass.replace('F','0')
    boarding_pass = boarding_pass.replace('L','0')
    binary = boarding_pass.replace('R','1')

    value = int(binary, 2)

    highest = max(value, highest)


print(highest)
    