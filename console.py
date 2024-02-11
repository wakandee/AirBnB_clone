#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        print()
        return True

    def help_quit(self):
        """
        Display help message for quit command.
        """
        print("Quit command to exit the program.")
        print()

    def help_EOF(self):
        """
        Display help message for EOF command.
        """
        print("Exit the program.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
