def calculate_total_scratchcards_from_file(file_path):
    def parse_line(line):
        parts = line.split('|')
        winning_numbers = list(map(int, parts[0].split()[2:]))
        your_numbers = list(map(int, parts[1].split()))
        return {"winning_numbers": winning_numbers, "your_numbers": your_numbers}

    def count_matches(winning, your):
        return len(set(winning) & set(your))

    cards = []
    with open(file_path, 'r') as file:
        for line in file:
            cards.append(parse_line(line.strip()))

    card_copies = [1] * len(cards)
    for i in range(len(cards)):
        matches = count_matches(cards[i]["winning_numbers"], cards[i]["your_numbers"])
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_copies[j] += card_copies[i]

    return sum(card_copies)

file_path = "2023\day__04\input.txt"
total_scratchcards = calculate_total_scratchcards_from_file(file_path)
print(total_scratchcards)