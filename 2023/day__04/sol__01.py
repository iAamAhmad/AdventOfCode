def calculate_total_points_from_file(file_path):
    def parse_line(line):
        parts = line.split('|')
        winning_numbers = list(map(int, parts[0].split()[2:]))  # Skip "Card X:"
        your_numbers = list(map(int, parts[1].split()))
        return {"winning_numbers": winning_numbers, "your_numbers": your_numbers}
    def calculate_card_points(card):
        matches = set(card["winning_numbers"]) & set(card["your_numbers"])
        return 2 ** (len(matches) - 1) if matches else 0
    total_points = 0
    with open(file_path, 'r') as file:
        for line in file:
            card = parse_line(line.strip())
            total_points += calculate_card_points(card)
    return total_points
file_path = "2023\day__04\input.txt"
total_points = calculate_total_points_from_file(file_path)
print(total_points)