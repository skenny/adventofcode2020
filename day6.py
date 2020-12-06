from functools import reduce

INPUT_FILE = "day6-input"

def read_input():
    groups = []
    with open(INPUT_FILE, 'r') as fin:
        group = []
        for line in fin.readlines():
            line = line.strip()
            if not line:
                groups.append(group)
                group = []
            else:
                group.append(line)
        groups.append(group)
    return groups

def count_anyone_answers(group):
    return len(set("".join(group)))

def count_everyone_answers(group):
    group_sets = list(map(set, group))
    return len(reduce(lambda total, group_set: total.intersection(group_set), group_sets[1:], group_sets[0]))

def sum(ints):
    return reduce(lambda total, group_count: total + group_count, ints)

def run_tests():
    test = lambda group, expected_count: print(group, 'is', expected_count, '?', count_anyone_answers(group) == expected_count)
    test(['abc'], 3)
    test(['a','b','c'], 3)
    test(['ab','ac'], 3)
    test(['a','a','a','a'], 1)
    test(['b'], 1)

def part1(groups):
    print('part 1', sum(map(count_anyone_answers, groups)))

def part2(groups):
    print('part 2', sum(map(count_everyone_answers, groups)))

def run_parts():
    groups = read_input()
    part1(groups)
    part2(groups)

run_tests()
run_parts()