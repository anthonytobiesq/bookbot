import sys

def print_book_report(word_count, char_counts, file_path=None):
    """
    Prints a report of the book analysis, including word count and character counts.
    """
    if file_path is None:
        file_path = sys.argv[1] if len(sys.argv) > 1 else "Unknown file"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    for item in char_counts:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")