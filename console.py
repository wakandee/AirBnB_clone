#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import sys


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

    def precmd(self, line):
        """Execute a command when it is entered."""
        if line == "python3 -m unittest discover tests":
            return line
        return cmd.Cmd.precmd(self, line)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "-c":
        HBNBCommand().onecmd(" ".join(sys.stdin.readlines()))
    else:
        HBNBCommand().cmdloop()
