#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return None
    tuple_c = len(sentence), sentence[0]
    return tuple_c
