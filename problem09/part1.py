with open('problem9_input.txt') as file:
    data = file.read().splitlines()

data = [int(i) for i in data]

preamble_size = 25

def two_sum_exists(nums, target):

    complement_map = {}

    for num in nums:
        if num in complement_map:
            return True
        else:
            complement_map[target - num] = num

    return False

for i in range(preamble_size, len(data)):

    target = data[i]
    previous_nums = data[i - preamble_size : i]

    if not two_sum_exists(previous_nums, target):
        print(target)

