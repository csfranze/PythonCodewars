# 1) Given some text, count each alphabetic character's occurrence in it, regardless of the case.

# 2) Let's suppose you have to use an old terminal window to represent the occurrencies of each character in a text-based horizontal bar graph. The terminal has a maximum width, provided as parameter (max_units_on_screen), and you have to abide by it.

# For example, if the maximum width is 80, your longest bar in the graph will be scaled to this size and all the others have to be represented and scaled proportionally to this size. Every unit of the bar will be represented by the character #. See examples below for typical output format.

# 3) The bars of the graph have to be sorted by number of occurrencies (from biggest to lowest, before getting scaled), then by alphabetic order of the letter (from a to z). Approximation of decimal numbers will happen on the lowest integer (for example: 57.1, 57.2, 57.68, 57.999 will all get reduced to 57 )


def count_and_print_graph(text, max_units_on_screen):

    # Eliminate everything from the text that isn't a letter.

    filtered_text = ""
    for char in text.lower():
        if char.isalpha():
            filtered_text += char

    # Get the unique characters and their count appearing in
    # the filtered text and put this info in a dictionary.

    unique_chars = []
    for char in filtered_text:
        if char not in unique_chars:
            unique_chars.append(char)
    unique_chars_count = [text.lower().count(char) for char in unique_chars]
    d = dict(zip(unique_chars, unique_chars_count))

    # Print a scaled bar graph using this dictionary.

    max_count = max(unique_chars_count)
    s = ""
    for element in sorted(sorted(d), key=d.get, reverse=True):
        s = s + "{}:".format(element) + "#" * int((max_units_on_screen*d[element])//max_count) + "\n"
    return s[:-1]
