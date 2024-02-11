#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("")
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
