with open('problem13_input.txt') as file:
    inputs = file.read().splitlines()

timestamp = int(inputs[0])

buses = inputs[1].split(',')

buses = list(filter(lambda x: x != 'x', buses))

buses = [int(bus) for bus in buses]

next_bus = min([(timestamp + bus - timestamp % bus, bus) for bus in buses], key = lambda x: x[0])

print(next_bus[1] * (next_bus[0] - timestamp))
