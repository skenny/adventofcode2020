INPUT_FILE = "day16-input"
TEST_INPUT_FILE = "day16-input-test"
TEST_INPUT_FILE_2 = "day16-input-test-2"

def read_input(file):
    rules = {}
    your_ticket = []
    nearby_tickets = []
    mode = 0

    with open(file, "r") as fin:
        for l in fin.readlines():
            l = l.strip()

            if len(l) == 0:
                continue

            if l == "your ticket:":
                mode = 1
                continue
            if l == "nearby tickets:":
                mode = 2
                continue

            if mode == 0:
                rule_name, rule_spec = l.split(": ")
                rule_ranges = []
                for rule_range in rule_spec.split(" or "):
                    low, high = rule_range.split("-")
                    rule_ranges.append(range(int(low), int(high) + 1))
                rules[rule_name] = rule_ranges
            if mode == 1:
                your_ticket = [int(v) for v in l.split(",")]
            if mode == 2:
                nearby_tickets.append([int(v) for v in l.split(",")])

    return (rules, your_ticket, nearby_tickets)

def validate_tickets(rules, tickets):
    invalid_count = 0
    valid_tickets = []

    for ticket in tickets:
        for n in ticket:
            valid = False
            for rule_ranges in rules.values():
                for rule_range in rule_ranges:
                    if n in rule_range:
                        valid = True
                        break
                if valid:
                    break

            if valid:
                valid_tickets.append(ticket)
            else:
                invalid_count += n

    return (invalid_count, valid_tickets)

def match_ticket_fields(rules, your_ticket, nearby_tickets):
    return

def run(label, input_file):
    rules, your_ticket, nearby_tickets = read_input(input_file)

    error_rate, valid_tickets = validate_tickets(rules, nearby_tickets)
    aaa = match_ticket_fields(rules, your_ticket, valid_tickets)

    print("{} 1: {}".format(label, error_rate))
    print("{} 2: {}".format(label, aaa))

run("test 1", TEST_INPUT_FILE)
run("test 2", TEST_INPUT_FILE_2)
run("part", INPUT_FILE)