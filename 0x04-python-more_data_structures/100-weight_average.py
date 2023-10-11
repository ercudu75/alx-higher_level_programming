#!/usr/bin/pyhton3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    score = weight = 0
    for tupel in my_list:
        score += tupel[0] * tupel[1]
        weight += tupel[1]
    return score / weight
