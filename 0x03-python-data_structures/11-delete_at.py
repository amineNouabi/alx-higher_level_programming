#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    copy = my_list.copy()
    my_list.clear()
    if idx > -1 and idx < len(copy):
        for i in range(len(copy)):
            if i == idx:
                continue
            my_list.append(copy[i])
    return my_list
