with open('problem5_input.txt') as file:
    inputs = file.readlines()

binary_passports = [int(i.strip().replace('B','1').replace('F','0').replace('L','0').replace('R','1'),2) for i in inputs]


binary_passports = sorted(binary_passports)

for i in range(0, len(binary_passports) - 1):
    if binary_passports[i] + 1 != binary_passports[i + 1]:
        print(binary_passports[i] + 1)