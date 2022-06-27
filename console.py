#!/usr/bin/python3
""""In this module the class HBNBCommand is defined"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class to make a python shell"""
    prompt = "(HBTN)"

    def do_quit(self, arg):
        """Usage: quit,
            quits the shell
        """
        exit()

    def do_EOF(self, arg):
        """Usage: EOF or CTRL+D
            quits the shell
        """
        print()
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
