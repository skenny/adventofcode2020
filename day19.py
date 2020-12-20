import re

INPUT_FILE = "day19-input"
TEST_INPUT_FILE = "day19-input-test"

def read_input(file):
    rules = {}
    messages = []

    mode = 0

    with open(file, "r") as fin:
        for line in fin.readlines():
            line = line.strip()

            if len(line) == 0:
                mode = 1
                continue

            if mode == 0:
                rule = line.split(": ")
                rule_num = int(rule[0])
                rule_spec = rule[1].replace('"', '')
                rules[rule_num] = rule_spec

            if mode == 1:
                messages.append(line)

    return rules, messages

def simplify(rules):
    rules_to_simplify = list(rules.keys())

    while len(rules_to_simplify) > 0:
        for rule_num in rules_to_simplify:
            rule_spec = rules[rule_num]
            #print("{}: {}".format(rule_num, rule_spec))
            if not any(char.isdigit() for char in rule_spec):
                #print("simple rule", rule_num, rule_spec)
                rules_to_simplify.remove(rule_num)
            else:
                new_rule_spec = ""
                for i in rule_spec.split(" "):
                    if i.isdigit() and not int(i) in rules_to_simplify:
                        simple_rule = rules[int(i)]
                        if len(simple_rule) == 1:
                            new_rule_spec += simple_rule + " "
                        else:
                            new_rule_spec += "(" + simple_rule + ") "
                    else:
                        new_rule_spec += i + " "
                rules[rule_num] = new_rule_spec.strip()

    return rules[0].replace(' ', '')

def count_valid_messages(rules, messages):
    target_rule_pattern = re.compile("^" + simplify(rules) + "$")    
    valid_messages = []
    for message in messages:
        if target_rule_pattern.match(message):
            valid_messages.append(message)
    return len(valid_messages)

def run(label, input_file):
    rules, messages = read_input(input_file)
    print("{} 1: {}".format(label, count_valid_messages(rules, messages)))

run("test", TEST_INPUT_FILE)
run("part", INPUT_FILE)