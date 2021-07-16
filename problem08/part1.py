with open('problem8_input.txt') as file:
    program = file.read().splitlines()

pointer = 0
accumulator = 0

executed_commands = set()

while pointer < len(program):
    counter = 1

    if pointer in executed_commands:
        print(accumulator)
        break
    else:
        executed_commands.add(pointer)

    next_line = program[pointer].split()

    instruction = next_line[0]
    value = int(next_line[1])

    if instruction == 'acc':
        accumulator += value
        counter = 1
    elif instruction == 'jmp':
        counter = value
    elif instruction == 'nop':
        counter = 1

    pointer += counter