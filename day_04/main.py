def number_of_matches(card):
    result = 0
    winning_numbers = card.split(":")[1].split("|")[0].split()
    numbers = card.split(":")[1].split("|")[1].split()

    for number in numbers:
        if number in winning_numbers:
            result += 1

    return result


def card_prize(current_card, number_of_matches):
    return [*range(current_card + 1, current_card + number_of_matches + 1)]


def part_1():
    result = 0

    file = open("day_04/example.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        num_matches = number_of_matches(line)

        if num_matches > 0:
            result += 2 ** (num_matches - 1)

    print("Total:", result)


def part_2():
    card_prizes = {}

    file = open("day_04/input.txt", "r")

    for i, line in enumerate(file):
        card = line.rstrip()
        num_matches = number_of_matches(card)
        card_prizes[i + 1] = card_prize(i + 1, num_matches)

    hand = list(card_prizes.keys())

    for card in hand:
        hand += card_prizes[card]

    print("Total:", len(hand))


part_1()
part_2()
