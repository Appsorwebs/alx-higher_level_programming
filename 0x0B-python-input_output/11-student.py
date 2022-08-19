#!/usr/bin/python3
"""
Contains class Student
that initializes public instance attributes first_name, last_name, and age,
and has public method to_json that returns dictionary representation
of requested attributes or all if none were requested
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, string)
        for JSON serialization of an object
        Return:
            Only return dict of attrs given to us
            Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if hasattr(self, att):
                    dic[att] = getattr(self, att)
            return dic

    def reload_from_json(self, json):
        """
        Return:
            Transfer all attributes of json to self
        """
        for key, value in json.items():
            setattr(self, key, value)
