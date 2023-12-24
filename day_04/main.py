def number_of_matches(card):
    result = 0
    winning_numbers = card.split(":")[1].split("|")[0].split()
    numbers = card.split(":")[1].split("|")[1].split()

    for number in numbers:
            if number in winning_numbers:
                result +=1
        
    return result

def main():
    result = 0

    file = open("day_04/example.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        num_matches = number_of_matches(line)

        if num_matches > 0:
            result += 2**(num_matches-1)
    
    print("Total:", result)

main()