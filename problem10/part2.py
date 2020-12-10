with open('problem10_input.txt') as file:
    jolts = file.read().splitlines()

jolts = [int(i) for i in jolts]

jolts = sorted(jolts)

jolts = [0] + jolts + [jolts[-1] + 3]

