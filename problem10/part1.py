with open('problem10_input.txt') as file:
    jolts = file.read().splitlines()

jolts = [int(i) for i in jolts]

jolts = sorted(jolts)

jolts = [0] + jolts + [jolts[-1] + 3]

difference_of_one = 0
difference_of_three = 0
last = 0

print(jolts)

for jolt in jolts:
    if jolt - last  == 1:
        difference_of_one += 1
    elif jolt - last == 3:
        difference_of_three += 1

    last = jolt

print(difference_of_one * difference_of_three)