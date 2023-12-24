def map_values(values, mapped_values, range):
    [ds, ss, l] = range

    for i, value in enumerate(values):
        if value >= ss and value < ss + l:
            mapped_values[i] = ds + (value - ss)

    return mapped_values


def handle_non_mapped_values(values, mapped_values):
    return [values[i] if x is None else x for i, x in enumerate(mapped_values)]


def part_1():
    values = []
    mapped_values = []
    step = ""

    file = open("day_05/example.txt", "r")
    lines = [l.rstrip() for l in file]

    for i, line in enumerate(lines):
        if i == 0:
            step = line.split(":")[0]
            values = [int(n) for n in line.split(":")[1].split()]
            mapped_values = values
        elif ":" in line:
            values = handle_non_mapped_values(values, mapped_values)
            mapped_values = [None] * len(values)
            print(values, step)
            step = line.split(":")[0]
        elif line == "":
            continue
        else:
            range = [int(n) for n in line.split()]
            mapped_values = map_values(values, mapped_values, range)

    values = handle_non_mapped_values(values, mapped_values)
    print(values, step)
    print("---")
    result = min(values)
    print("Result:", result)


def calculate_seeds(line):
    result = []
    values = [int(n) for n in line.split(":")[1].split()]

    for i in range(0, len(values), 2):
        seed = values[i]
        l = values[i + 1]
        result += list(range(seed, seed + l))

    return result


def part_2():
    values = []
    mapped_values = []
    step = ""

    file = open("day_05/example.txt", "r")
    lines = [l.rstrip() for l in file]

    for i, line in enumerate(lines):
        if i == 0:
            step = line.split(":")[0]
            values = calculate_seeds(line)
            mapped_values = values
        elif ":" in line:
            values = handle_non_mapped_values(values, mapped_values)
            mapped_values = [None] * len(values)
            print(values, step)
            step = line.split(":")[0]
        elif line == "":
            continue
        else:
            range = [int(n) for n in line.split()]
            mapped_values = map_values(values, mapped_values, range)

    values = handle_non_mapped_values(values, mapped_values)
    print(values, step)
    print("---")
    result = min(values)
    print("Result:", result)


part_1()
part_2()
