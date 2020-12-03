with open('problem3_input.txt') as file:
    inputs = file.readlines()

slopes = [i.strip() for i in inputs]

count = 0
x = 0

line_length = len(slopes[0])

print(line_length)

for slope in slopes:
    if slope[x % line_length] == '#':
        count += 1

    print(slope)
    print(x)
    print(slope[x % line_length])
    
    x += 3
    

    

print(count)