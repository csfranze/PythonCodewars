# Take an array and remove every second element out of that array. Always keep the first element and start removing with the next element.

# Example:

# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]


def remove_every_other(my_list):
    return [my_list[i] for i in range(0, len(my_list), 2)]
