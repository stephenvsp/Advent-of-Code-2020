with open('problem9_input.txt') as file:
    data = file.read().splitlines()

data = [int(i) for i in data]

target = 1398413738
front = 0
back = 0

while (sum(data[back:front]) != target):
    total = sum(data[back:front])

    if total < target:
        front += 1
    elif total > target:
        back += 1


continuous_set = data[521:538]

print(min(continuous_set) + max(continuous_set))