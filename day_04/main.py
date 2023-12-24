def main():
    result = 0

    file = open("day_04/input.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        total = 0
        winning_numbers = line.split(":")[1].split("|")[0].split()
        numbers = line.split(":")[1].split("|")[1].split()

        for number in numbers:
            if number in winning_numbers:
                if total == 0:
                    total += 1
                else:
                    total *= 2
        
        result +=total
    
    print("Total:", result)

main()