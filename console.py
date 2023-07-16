#!/usr/bin/python3
import cmd
"""Module that contains 'HBNBCommand' class"""


class HBNBCommand(cmd.Cmd):
    """'HBNBCommand' Class declaration and definition"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Method to exit the cli console program"""
        return True

    def do_quit(self, line):
        """Method to exit the cli console program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
