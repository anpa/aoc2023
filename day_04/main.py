def number_of_matches(card):
    result = 0
    winning_numbers = card.split(":")[1].split("|")[0].split()
    numbers = card.split(":")[1].split("|")[1].split()

    for number in numbers:
            if number in winning_numbers:
                result +=1
        
    return result

def part_1():
    result = 0

    file = open("day_04/example.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        num_matches = number_of_matches(line)

        if num_matches > 0:
            result += 2**(num_matches-1)
    
    print("Total:", result)

def part_2():
    result = 0
    all_cards = {}

    file = open("day_04/input.txt", "r")

    for i,line in enumerate(file):
        card = line.rstrip()
        all_cards[i+1] = number_of_matches(card)
    
    hand = list(all_cards.keys())

    for card in hand:
        num_matches = all_cards[card]
        
        for n in range(card+1, card + num_matches + 1):
            hand.append(n)
    
    print("Total:", len(hand))

part_1()
part_2()