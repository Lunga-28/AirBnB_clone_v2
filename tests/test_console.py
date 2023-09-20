#!/usr/bin/python3
''' suite console'''

import os
import sys
import models
import unittest
import pep8
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):

    def test_pep8_console(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        sys.stdout = self.backup

    def create(self):
        return HBNBCommand()

    def test_quit(self):
        ''' '''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        ''' '''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show(self):
        '''

        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(isinstance(x, str))

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show_class_name(self):

        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show_class_name(self):

        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_show_no_instance_found(self):
        '''
            show error message
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "124356876")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db',
        "won't work in db")
    def test_create_fileStorage(self):

        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):

        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doest_exist(self):

        console = self.create()
        console.onecmd("create Binita")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

  
