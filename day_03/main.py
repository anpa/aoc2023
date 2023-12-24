def is_adjacent_to_symbol(matrix, n, coord):
    result = False
    [x, y] = coord

    for xi in range(x - 1, x + 2):
        for yi in range(y - len(n), y + 2):
            # check if coordinates within bounds
            if (xi >= 0 and yi >= 0 and xi < len(matrix) and yi < len(matrix[0])):
                # check if adjacent symbol
                if not (matrix[xi][yi].isdigit() or matrix[xi][yi] == "."):
                    result |= True
    
    return result

def part_1():
    matrix = []
    result = 0

    file = open("day_03/input.txt", "r")
    lines = [l.rstrip() for l in file]

    # Turn engine schematic into a matrix
    for line in lines:
        row = list(line)
        matrix.append(row)
    
    # Parse numbers
    for x, row in enumerate(matrix):
        n = ""
        for y, column in enumerate(row):
            if column.isdigit():
                n += column
                
                if y == len(row) - 1 or not matrix[x][y+1].isdigit():
                    if is_adjacent_to_symbol(matrix, n, [x, y]):
                        result += int(n)
                    n = ""
                    
    print("Total:", result)

part_1()