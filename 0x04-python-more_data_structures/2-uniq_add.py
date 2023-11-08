#!/usr/bin/python3
def uniq_add(my_list=[]):
    dic = {}
    sum = 0
    for i in my_list:
        if i not in dic:
            sum += i
            dic[i] = 1
    return sum
