#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position without modifying the original list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list

    original_list = [1, 2, 3, 4, 5,]

    modified_list = new_in_list(original_list, 3, 9)
    print(modified_list)

    modified_list = new_in_list(original_list, 10, 6)
    print(modified_list)

    modified_list = new_in_list(original_list, -1, 7)
    print(modified_list)
