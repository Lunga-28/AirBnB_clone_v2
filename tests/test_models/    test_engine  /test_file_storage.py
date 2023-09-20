#!/usr/bin/python3
'''

'''

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage

class testFileStorage(unittest.TestCase):
    '''

    '''
    def setUp(self):

        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        '''

        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_delete(self):
        new_state = State()
        new_state.name = "California***********"
        fs = FileStorage()
        fs.new(new_state)
        fs.save()
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()
        flag = 1
        if new_state.id in content:
            flag = 0
        self.assertTrue(flag == 0)
        fs.delete(new_state)
        fs.save()
        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()
        flag = 0
        if new_state.id in content:
            flag = 1
        self.assertTrue(flag == 0)

    def test_new_method(self):

        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_objects_value_type(self):
        '''

        '''
        self.storage.new(self.my_model)
        key = str(self.my_model.__class__.__name__ + "." + self.my_model.id)
        val = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.my_model, type(val))

    def test_save_file_exists(self):
        '''
            Tests that a file gets created with the name file.json
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        '''
            Testing the contents of the files inside the file.json
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(isinstance(content, dict))

    def test_the_type_file_content(self):

        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reaload_without_file(self):

        try:
            self.storage.reload()
            self.assertTrue(True)
        except BaseException:
            self.assertTrue(False)
