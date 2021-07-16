with open('problem3_input.txt') as file:
    inputs = file.readlines()

slopes = [i.strip() for i in inputs]

count = 0
x = 0
y = 0

line_length = len(slopes[0])

while y < len(slopes):
    if slopes[y][x % line_length] == '#':
        count += 1
    
    x += 3
    y += 1
    

    

print(count)