digits = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
]

def get_lower_index_for_number(input, n):
    word = digits[n-1]

    word_index = input.find(word)
    number_index = input.find(str(n))

    if word_index == -1 and number_index == -1:
        return -1
    else:
        return min(i for i in [word_index, number_index] if i >= 0)

def get_higher_index_for_number(input, n):
    word = digits[n-1]

    word_index = input.rfind(word)
    number_index = input.rfind(str(n))

    if word_index == -1 and number_index == -1:
        return -1
    else:
        return max(i for i in [word_index, number_index])

def find_first_value(input):
    result = []

    for n in range(1,10):
        lower_index = get_lower_index_for_number(input, n)
        result.append(lower_index)
    
    min_index = min(i for i in result if i >= 0)
    number = result.index(min_index) + 1
    return [min_index, number]

def find_last_value(input):
    result = []

    for n in range(1,10):
        higher_index = get_higher_index_for_number(input, n)
        result.append(higher_index)
    
    max_index = max(i for i in result)
    number = result.index(max_index) + 1
    return [max_index, number]

def main():
    result = 0

    file = open("day_01/input.txt", "r")
    lines = [l.rstrip() for l in file]

    for line in lines:
        first = find_first_value(line)
        last = find_last_value(line)
        calibration_value = int(str(first[1]) + str(last[1]))
        
        print(line, first, last, calibration_value)
        result += calibration_value
    
    print("Total:", result)

main()