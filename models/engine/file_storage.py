#!/usr/bin/python3
'''
    class FileStorage
'''
import json
import models

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        obje = {}
        if cls is None:
            return (self.__objects)
        else:
            new = {obj: key for obj, key in self.__objects.items()
                   if type(key) == cls}
            return (new)

    def new(self, obj):

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):

        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def delete(self, obj=None):
        """

        """
        if not obj:
            return
        key = '{}.{}'.format(type(obj).__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]
            self.save()

    def reload(self):

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def close(self):

        self.reload()
