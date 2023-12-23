limits = { "red": 12, "green": 13, "blue": 14 }

def is_game_possible(game):
    for set in game:
        for group in set.split(", "):
            [number, color] = group.split(" ")

            if limits[color] < int(number):
                return False
    
    return True


def part_1():
    result = 0

    file = open("day_02/input.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        number = int(line.split(":")[0].split(" ")[1])
        game = line.split(": ")[1].split("; ")

        if is_game_possible(game):
            result += number
    
    print("Total: ", result)
        

def fewest_number_of_cubes(game):
    max_red = 0
    max_green = 0
    max_blue = 0

    for set in game:
        for group in set.split(", "):
            [number, color] = group.split(" ")

            if (color == "red"):
                max_red = max(max_red, int(number))
            elif (color == "green"):
                max_green = max(max_green, int(number))
            elif (color == "blue"):
                max_blue = max(max_blue, int(number))
    
    return [max_red, max_green, max_blue]

def part_2():
    result = 0

    file = open("day_02/input.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        number = int(line.split(":")[0].split(" ")[1])
        game = line.split(": ")[1].split("; ")

        [r,g,b] = fewest_number_of_cubes(game)
        result += r * g * b
    
    print("Total: ", result)


part_1()
part_2()