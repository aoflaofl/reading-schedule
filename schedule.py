from typing import List, Tuple

def calculate_reading_schedule(word_counts: List[int], num_days: int) -> List[Tuple[int, int]]:
    if not word_counts or num_days <= 0:
        return []

    total_words = sum(word_counts)
    page_target = total_words // num_days
    day_ranges = []
    current_day_start = 0
    sum_pages = 0

    for idx, word_count in enumerate(word_counts):
        sum_pages += word_count
        if sum_pages >= page_target:
            day_ranges.append((current_day_start, idx))
            current_day_start = idx + 1
            sum_pages = 0

    if current_day_start < len(word_counts):
        day_ranges.append((current_day_start, len(word_counts) - 1))

    return day_ranges

def print_reading_schedule(day_ranges: List[Tuple[int, int]], word_counts: List[int]) -> None:
    for day, (start, end) in enumerate(day_ranges, 1):
        chapters = [f"Chapter {i + 1}" for i in range(start, end + 1)]
        total_words = sum(word_counts[start:end + 1])
        print(f"Day {day} reading {', '.join(chapters)} will read {total_words} words")

def main():
    word_counts = [7351, 10012, 11311, 9763, 5957, 5196, 6502, 5501, 6694, 6251, 5905, 9468, 8805]
    num_days = 14
    day_ranges = calculate_reading_schedule(word_counts, num_days)
    print_reading_schedule(day_ranges, word_counts)

if __name__ == "__main__":
    main()
