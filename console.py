#!/usr/bin/python3
"""
    console for the BnB project.
"""
import cmd
import json
import shlex
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import classes


class HBNBCommand(cmd.Cmd):


    prompt = ("(hbnb) ")
    all_classes = classes

    def do_quit(self, args):
        return True

    def do_EOF(self, args):

        return True

    def do_create(self, line):

        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")
        else:
            cls = self.all_classes[args[0]]
            obj = cls()
            if len(args) > 1:
                for i in range(1, len(args)):
                    pair = args[i].split('=')
                    if len(pair) == 2:
                        pair[1] = pair[1].replace('_', ' ')
                        try:
                            setattr(obj, pair[0], eval(pair[1]))
                        except (SyntaxError, NameError):
                            setattr(obj, pair[0], pair[1])
            print(obj.id)
            models.storage.save()

    def do_show(self, line):

        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):

        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                objs.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):

        args = shlex.split(line)
        obj_list = []
        if len(args) >= 1:
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
            else:
                objs = models.storage.all(args[0])
                for key, obj in objs.items():
                    if key.startswith(args[0]):
                        obj_list.append(obj)
                print(obj_list)
        else:
            objs = models.storage.all()
            for obj in objs.values():
                obj_list.append(obj)
            print(obj_list)

    def do_update(self, args):

        models.storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = models.storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):

        pass

    def do_count(self, line):

        args = shlex.split(line)
        if len(args) >= 1:
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
            else:
                objs = models.storage.all(args[0])
                print(len(objs))
        else:
            objs = models.storage.all()
            print(len(objs))

    def default(self, args):

        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))
        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":

    HBNBCommand().cmdloop()
