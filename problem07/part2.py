with open('problem7_input.txt') as file:
    rules = file.read().splitlines()

bag_map = {}

for rule in rules:
    rule = rule.split(' contain ')

    container = rule[0][:-4].strip()
    contents = rule[1].split(', ')

    map_values = []

    for content in contents:
        if content != 'no other bags.':
            content = content.replace('.', '')
            content = content.replace('bags','')
            content = content.replace('bag','')

            num = content[0]
            bag_type = content[2:].strip()

            map_values.append((num, bag_type))

    bag_map[container] = map_values

def size_of_bag(container):
    contents = bag_map[container]
    
    total = 0

    for content in contents:
        total += int(content[0])
        total += int(content[0]) * size_of_bag(content[1])

    return total


print(size_of_bag('shiny gold'))
