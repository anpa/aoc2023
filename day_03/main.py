import math

def is_symbol(char):
    return not (char.isdigit() or char == ".")

def is_coord_valid(x, y, matrix):
    if x < 0 or y < 0:
        return False
    else:
        try:
            matrix[x][y]
            return True
        except IndexError:
            return False

def adjacent_symbol_coord(matrix, n, coord):
    [x, y] = coord

    for xi in range(x - 1, x + 2):
        for yi in range(y - len(n), y + 2):
            if is_coord_valid(xi, yi, matrix) and is_symbol(matrix[xi][yi]):
                return [xi, yi]
    
    return None

def file_to_matrix(filename):
    matrix = []
    file = open(filename, "r")

    for line in file:
        row = list(line.rstrip())
        matrix.append(row)

    return matrix

def part_1():
    result = 0

    matrix = file_to_matrix("day_03/input.txt")

    # Parse numbers
    for x, row in enumerate(matrix):
        n = ""
        for y, column in enumerate(row):
            if column.isdigit():
                n += column

                if not (y < len(row) - 1 and matrix[x][y+1].isdigit()):
                    if adjacent_symbol_coord(matrix, n, [x, y]) != None:
                        result += int(n)
                    n = ""
                    
    print("Total:", result)

def part_2():
    result = 0
    findings = {}

    matrix = file_to_matrix("day_03/input.txt")

    # Parse numbers
    for x, row in enumerate(matrix):
        n = ""
        for y, column in enumerate(row):
            if column.isdigit():
                n += column

                if not (y < len(row) - 1 and matrix[x][y+1].isdigit()):
                    symbol_coord = adjacent_symbol_coord(matrix, n, [x, y])

                    if symbol_coord != None:
                        [sx, sy] = symbol_coord
                        symbol = matrix[sx][sy]

                        if symbol == "*":
                            if (sx, sy) in findings:
                                findings[(sx,sy)].append(int(n))
                            else:
                                findings[(sx,sy)] = [int(n)]

                    n = ""

    for value in findings.values():
        if len(value) == 2:
            result += math.prod(value)
    
    print("Total:", result)

part_1()
part_2()