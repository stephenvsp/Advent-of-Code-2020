with open('problem5_input.txt') as file:
    inputs = file.readlines()

print(max([int(i.strip().replace('B','1').replace('F','0').replace('L','0').replace('R','1'), 2) for i in inputs]))
    