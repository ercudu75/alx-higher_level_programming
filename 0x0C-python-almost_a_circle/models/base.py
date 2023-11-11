#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dict = []
        if list_objs is not None:  # Ensure list_objs is not None before iterating
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_dict))
