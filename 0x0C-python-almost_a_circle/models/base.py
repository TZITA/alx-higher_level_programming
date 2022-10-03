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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            1. json_string: string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            1. dictionary: A dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                tmp = cls(1, 1)
            else:
                tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filen = str(cls.__name__) + ".json"
        try:
            with open(filen, "r") as file_n:
                list_dictionary = Base.from_json_string(file_n.read())
                return [cls.create(**d) for d in list_dictionary]
        except IOError:
            return []
