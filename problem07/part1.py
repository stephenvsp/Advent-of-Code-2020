with open('problem7_input.txt') as file:
    inputs = file.readlines()

rules = [i.strip() for i in inputs]

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

def can_hold_shiny_gold_bag(container):
    contents = bag_map[container]

    if contents == []:
        return False
    else:
        for content in contents:
            if content[1] == 'shiny gold':
                return True
            else:
                if can_hold_shiny_gold_bag(content[1]):
                    return True
        return False

count = 0

for key in bag_map.keys():
    if can_hold_shiny_gold_bag(key):
        count += 1

print(count)
