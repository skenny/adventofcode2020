import re

INPUT_FILE = "day7-input"

INPUT_REGEX_EMPTY = r"(\w+ \w+) bags contain no other bags."
INPUT_REGEX_NON_EMPTY = r"(\w+ \w+) bags contain (.+)"
INPUT_REGEX_NON_EMPTY_CONTENTS = r"(\d) (\w+ \w+) bags?[.,]"

def read_input():
    with open(INPUT_FILE, "r") as fin:
        return fin.readlines()

def parse_rules(input):
    return [parse_rule(line) for line in input]

def parse_rule(description):
    empty_matches = re.findall(INPUT_REGEX_EMPTY, description)
    if len(empty_matches) > 0:
        return (empty_matches[0], [])
    else:
        non_empty_matches = re.findall(INPUT_REGEX_NON_EMPTY, description)[0]
        bag = non_empty_matches[0]
        contents = list(map(lambda t: (int(t[0]), t[1]), re.findall(INPUT_REGEX_NON_EMPTY_CONTENTS, non_empty_matches[1])))
        return (bag, contents)

def count_bag_holders(target_bag, rules):
    bags_to_search = list(rules.keys())
    bags_to_search.remove(target_bag)

    count = 0
    for s in bags_to_search:
        if can_bag_hold_target_bag(s, target_bag, rules):
            count += 1
    return count

def can_bag_hold_target_bag(bag, target_bag, rules):
    inner_bags = list(map(lambda t: t[1], rules[bag]))

    if target_bag in inner_bags:
        return True

    for inner_bag in inner_bags:
        if can_bag_hold_target_bag(inner_bag, target_bag, rules):
            return True
            
    return False

def count_inner_bags(bag, rules):
    count = 0
    for num, inner_bag in rules[bag]:
        count += num + (num * count_inner_bags(inner_bag, rules))
    return count

def run_tests():
    inputs = [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]
    rules = parse_rules(inputs)
    rules_dict = dict(rules)
    
    for i, input in enumerate(inputs):
        print('{} -> {}'.format(input, rules[i]))

    target_bag = "shiny gold"
    print("test 1: a {} bag can be held by {} other bags".format(target_bag, count_bag_holders(target_bag, rules_dict)))
    print("test 2: a {} bag must contain {} other bags".format(target_bag, count_inner_bags(target_bag, rules_dict)))

def run_parts():
    rules = dict(parse_rules(read_input()))
    print("part 1", count_bag_holders("shiny gold", rules))
    print("part 2", count_inner_bags("shiny gold", rules))

run_tests()
run_parts()