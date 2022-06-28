#!/usr/bin/python3
""""In this module the class HBNBCommand is defined"""

import cmd
from models import storage, classes
from re import search
import json


class HBNBCommand(cmd.Cmd):
    """Class to make a python shell"""
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity", "Place",
                     "City", "State", "Review"]

    @staticmethod
    def validate_params(params, case):
        """
        Validate the params passed for the customize methods (CRUD)
        Args:
            - params : str[]
            - case : int
        """
        if (case >= 0):
            if not (params):
                print("** class name missing **")
                return (1)

            if (params[0] not in HBNBCommand.valid_classes):
                print("** class doesn't exist **")
                return (1)

        if (case >= 1):
            len_params = len(params)

            if (len_params == 1):
                print("** instance id missing **")
                return (1)
            if not (storage.all().get(f"{params[0]}.{params[1]}", None)):
                print("** no instance found **")
                return (1)

        if (case == 2):
            if (len_params == 2):
                print("** attribute name missing **")
                return (1)

        #     if (len_params == 3):
        #         print("** value missing **")
        #         return (1)

        return (0)

    def emptyline(self):
        """Overwrites the standard behavior when nothing is entered"""
        pass

    def do_quit(self, arg):
        """Usage: quit,\nquits the shell"""
        exit()

    def do_EOF(self, arg):
        """Usage: EOF or CTRL+D\nquits the shell"""
        print()
        exit()

    def do_create(self, arg):
        """Usage: create <class_name>
create: Create a new instance of a class"""
        params = arg.split()

        if not (HBNBCommand.validate_params(params, 0)):
            new_model = classes[params[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """Usage: show <class_name> <id>
show: Show an instance with the id"""
        params = arg.split()

        if not (HBNBCommand.validate_params(params, 1)):
            print(storage.all().get(f"{params[0]}.{params[1]}"))

    def do_destroy(self, arg):
        """Usage: destroy <class_name> <id>
destroy: Destroy an instance with the id"""
        params = arg.split()

        if not (HBNBCommand.validate_params(params, 1)):
            element = storage.all()
            del element[f"{params[0]}.{params[1]}"]
            storage.save()

    def do_all(self, arg):
        """Usage: all <BaseModel> | all
all: Display all instances or specific one"""
        params = arg.split()
        values = storage.all().values()

        if not (params):
            print([str(value) for value in values])
            return

        if (params[0] not in HBNBCommand.valid_classes):
            print("** class doesn't exist **")
        else:
            name = params[0]
            filt = filter(lambda x: x.__class__.__name__ == name, values)
            print([str(i) for i in list(filt)])

    def do_update(self, arg):
        """Usage: update <class name> <id> <attr name> <attr value>
update: changes or adds an attribute to an instance"""
        reg = search("(\{.*\})", arg)
        
        params = arg.split()

        if not (HBNBCommand.validate_params(params, 2)):
            if (reg):
                dct = json.loads(reg.group(1))
            else:
                if (len(params) == 3):
                    print("** value missing **")
                    return
                dct = {f"{params[2]}": params[3]}
            for i in dct.keys():
                if (i in ["id", "created_at", "updated_at"]):
                    print("Forbbiden")
                    return
                if (type(dct[i]) is str):
                    if (dct[i].isdigit()):
                        dct[i] = int(dct[i])
                    else:
                        try:
                            dct[i] = float(dct[i])
                        except ValueError:
                            pass
            storage.all()[f"{params[0]}.{params[1]}"].__dict__.update(**dct)
            storage.save()
    
    def precmd(self, line):
        regex = search("^(\w+)\.(\w+)\((.*)\)$", line)
        if (regex):
            cmds = ["all", "count", "destroy", "show", "update"]
            class_name = regex.group(1)
            cmdd = regex.group(2)
            args = regex.group(3)
            if (cmdd in cmds):
                if (cmdd == "all"):
                    query = f"{cmdd} {args}"
                if (cmdd == "update"):
                    dct = search("(\{.*\})", args)
                    arg_1 = args.split(',')
                    if (dct):
                        query = f"{cmdd} {class_name} {arg_1[0]} {dct.group(1)}"
                    else:
                        query = f"{cmdd} {class_name} {''.join(arg_1)}"
                elif (cmdd == "count"):
                    # ??
                    if (class_name not in HBNBCommand.valid_classes):
                        return line
                    storage_keys = storage.all().keys()
                    print(len([i for i in storage_keys if i.split('.')[0] == class_name]))
                    return "\n"
                else:
                    query = f"{cmdd} {class_name} {args}"
                return query

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
