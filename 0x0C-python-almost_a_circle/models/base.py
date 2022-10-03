#!/usr/bin/python3
"""Defines a class Base."""
import json


class Base:
    """Class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of class base with one parameter id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list of dictionaries.
        Args:
            1. list_dictionary: List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            1. list_objs: List of inherited base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionary = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(list_dictionary))
