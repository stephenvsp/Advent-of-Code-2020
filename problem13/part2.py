from functools import reduce

with open('problem13_input.txt') as file:
    inputs = file.read().splitlines()

timestamp = int(inputs[0])

buses = inputs[1].split(',')

buses = [(i, bus) for i, bus in enumerate(buses)]

buses = list(filter(lambda x: x[1] != 'x', buses))

buses = [(bus[0], int(bus[1])) for bus in buses]

# print(buses)
buses = [(((0 - bus[0] + bus[1]) % bus[1]), bus[1]) for bus in buses]

modulos = [bus[1] for bus in buses]
values = [bus[0] for bus in buses]

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(chinese_remainder(modulos, values))
