#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is within the valid range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Use list slicing to delete the element at the specified index
    return my_list[:idx] + my_list[idx + 1:]
