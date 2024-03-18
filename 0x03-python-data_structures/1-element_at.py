#!usr/bin/python3

def element_at(my_list, idx):
    """retrieve element function

    if idx is negative, the function should return none
    if idx is out of range (> of number of element in my_list)
    you are not allowed to import any module
    you are not allowed to use try/except
    """
    if idx > len(my_list)-1 or idx < 0:
        return None
    else:
        return my_list[idx]
        else:
            return my_list[idx]
