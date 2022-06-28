#!/usr/bin/python3
""""In this module the class HBNBCommand is defined"""

import cmd
from models.base_model import BaseModel, storage


class HBNBCommand(cmd.Cmd):
    """Class to make a python shell"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Usage: quit,\nquits the shell"""
        exit()

    def do_EOF(self, arg):
        """Usage: EOF or CTRL+D\nquits the shell"""
        print()
        exit()

    def do_create(self, arg):
        """"""
        params = arg.split()

        if not (params):
            print("** class name missing **")
            return

        if (params[0] not in ["BaseModel"]):
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)


    def do_show(self, arg):
        """"""
        params = arg.split()
        if not (params):
            print("** class name missing **")
            return

        if (params[0] not in ["BaseModel"]):
            print("** class doesn't exist **")
            return

        len_params = len(params)

        if (len_params == 1):
            print("** instance id missing **")
            return

        if not (storage.all().get(f"{params[0]}.{params[1]}", None)):
            print("** no instance found **")
            return

        print(storage.all().get(f"BaseModel.{params[1]}"))


    def do_destroy(self, arg):
        """"""
        params = arg.split()

        if not (params):
            print("** class name missing **")
            return

        if (params[0] not in ["BaseModel"]):
            print("** class doesn't exist **")
            return

        len_params = len(params)

        if (len_params == 1):
            print("** instance id missing **")
            return

        if not (storage.all().get(f"{params[0]}.{params[1]}", None)):
            print("** no instance found **")
            return

        element = storage.all()
        del element[f"{params[0]}.{params[1]}"]
        storage.save()


    def do_all(self, arg):
        """"""
        params = arg.split()

        if not (params):
            print(storage.all())
            return

        if (params[0] not in ["BaseModel"]):
            print("** class doesn't exist **")
        else:
            print(storage.all())

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"""
        params = arg.split()

        if not (params):
            print("** class name missing **")
            return

        class_name = params[0]

        if (class_name not in ["BaseModel"]):
            print("** class doesn't exist **")
            return

        len_params = len(params)

        if (len_params == 1):
            print("** instance id missing **")
            return

        id = params[1]

        obj = storage.all().get(f"{class_name}.{id}", None)

        if not (obj):
            print("** no instance found **")
            return

        if (len_params == 2):
            print("** attribute name missing **")
            return

        if (len_params == 3):
            print("** value missing **")
            return

        key = params[2]
        value = params[3]

        if (key in ["id", "created_at", "updated_at"]):
            print("Forbbiden")

        if (value.isdigit()):
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass

        storage.all()[f"{class_name}.{id}"][key] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
