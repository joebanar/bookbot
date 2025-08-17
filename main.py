import sys
from stats import get_word_count, get_file_contents, get_character_count, sort_by_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    def main():
        file = sys.argv[1]
        file_contents = get_file_contents(file)
        words = get_word_count(file_contents)
        char_count = get_character_count(file_contents)
        sorted_counts = sort_by_count(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}")
        print("----------- Word Count ----------")
        print(f"Found {len(words)} total words")
        print("--------- Character Count -------")
        for key, value in sorted_counts.items():
            if key.isalpha():
                print(f"{key}: {value}")
    main()