#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """This will return a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        class_name = cls.__name__
        dct = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == class_name:
                dct[key] = self.__objects[key]
        return dct

    def new(self, obj):
        """This will add new object to storage dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
            )

    def save(self):
        """This will Save storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.review import Review
        from models.city import City

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ 
            This will delete the object from the attribute
        """
        if obj is None:
            return
        object_key = obj.to_dict()['__class__'] + '.' + obj.id
        if object_key in self.__objects.keys():
            del self.__objects[object_key]

    def close(self):
        """Will Call the reload method"""
        self.reload()
