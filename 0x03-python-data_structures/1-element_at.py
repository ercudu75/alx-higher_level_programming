#!/usr/bin/pyhton3
def element_at(my_list, idx):
    if int(idx) < 0 or int(idx) > len(my_list):
        return None
    else:
        return my_list.index(idx)
