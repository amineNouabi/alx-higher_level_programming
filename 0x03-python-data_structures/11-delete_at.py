#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    copy = my_list.copy()
    my_list.clear()
    for i in range(len(copy)):
        if i == idx:
            continue
        my_list.append(copy[i])
    return my_list
