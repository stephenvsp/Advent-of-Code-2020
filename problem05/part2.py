with open('problem5_input.txt') as file:
    inputs = file.readlines()

boarding_passes = [i.strip() for i in inputs]

binary_passports = []

for boarding_pass in boarding_passes:

    boarding_pass = boarding_pass.replace('B','1')
    boarding_pass = boarding_pass.replace('F','0')
    boarding_pass = boarding_pass.replace('L','0')
    binary = boarding_pass.replace('R','1')

    value = int(binary, 2)

    binary_passports.append(value)


binary_passports = sorted(binary_passports)

for i in range(0, len(binary_passports) - 1):
    if binary_passports[i] + 1 != binary_passports[i + 1]:
        print(binary_passports[i] + 1)