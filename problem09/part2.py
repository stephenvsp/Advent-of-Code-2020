with open('problem9_input.txt') as file:
    data = file.read().splitlines()

data = [int(i) for i in data]

target = 1398413738
front = 0
back = 0

total = 0

while (total != target):

    if total < target:
        total += data[front]
        front += 1
        
    elif total > target:
        total -= data[back]
        back += 1


continuous_set = data[back:front]

print(min(continuous_set) + max(continuous_set))