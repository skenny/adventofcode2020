input = []
with open('day4-input', 'r') as fin:
    record_num = 0
    for line in fin.readlines():
        line = line.strip()
        if len(line) == 0:
            record_num += 1
        else:
            if record_num + 1 > len(input):
                input.append({})
            record = input[record_num]
            for part in line.split(" "):
                parts = part.split(":")
                record[parts[0]] = parts[1]

def day1():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0
    for record in input:
        valid = True
        for required_field in required_fields:
            # this could be optimized to short-circuit as soon as there's a missing required field but meh
            valid &= required_field in record
        if valid:
            valid_count += 1
    print("part 1: of", len(input), "records,", valid_count, "are valid passports")

day1()