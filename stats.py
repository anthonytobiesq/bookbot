def word_count(text):
    """
    Counts the number of words in the given text.
    """
    words = text.split()  # Split the text into words
    return len(words)  # Return the total word count


def get_chars_dict(text):
    """
    Counts the occurrences of each character in the text and returns a dictionary.
    """
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sorted_list_of_dictionaries(chars):
    """
    Converts the character dictionary into a sorted list of dictionaries.
    Each dictionary contains a character and its count.
    """
    char_list = [{"char": key, "num": value} for key, value in chars.items()]
    char_list.sort(key=lambda d: d["num"], reverse=True)  # Sort by count in descending order
    return char_list