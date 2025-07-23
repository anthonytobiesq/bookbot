import sys
from stats import word_count, get_chars_dict, sorted_list_of_dictionaries
from print import print_book_report


def get_book_text(file_path):
    """
    Reads the content of a text file and returns it as a string.
    Handles errors like FileNotFoundError gracefully.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'. Please check the path and try again.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for file '{file_path}'.")
        sys.exit(1)


def filter_alphabetic(sorted_char_counts):
    """
    Filters only alphabetic characters from the sorted list of dictionaries.
    """
    return [item for item in sorted_char_counts if item["char"].isalpha()]


def main():
    """
    Main function to process the book text and generate a report.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)

    # Process the book text
    print("Processing book text...")
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

    dict_char_count = get_chars_dict(book_text)
    sorted_char_counts = sorted_list_of_dictionaries(dict_char_count)

    # Filter only alphabetic characters
    alpha_only = filter_alphabetic(sorted_char_counts)

    # Generate and print the book report
    print_book_report(num_words, alpha_only, file_path)


if __name__ == "__main__":
    main()
    print("Exiting the program.")