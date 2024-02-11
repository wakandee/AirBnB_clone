#!/usr/bin/python3
"""Console module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF to exit the program."""
        return True

    def emptyline(self):
        """Empty line should not execute anything."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
