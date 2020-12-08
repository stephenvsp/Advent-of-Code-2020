with open('problem8_input.txt') as file:
    game = file.read().splitlines()

def run_program(program):
    inf_loop = False
    pointer = 0
    accumulator = 0

    executed_commands = set()

    while pointer < len(program):
        counter = 1

        if pointer in executed_commands:
            inf_loop = True
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
    
    if not inf_loop:
        print(accumulator)


for i in range(0, len(game)):
    if 'acc' not in game[i]:
        
        temp_game = game.copy()
        if 'jmp' in temp_game[i]:
            temp_game[i] = temp_game[i].replace('jmp','nop')
        elif 'nop' in temp_game[i]:
            temp_game[i] = temp_game[i].replace('nop','jmp')

        run_program(temp_game)


