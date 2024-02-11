#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter."""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create command to create a new instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show command to display string representation of an instance."""
        if not arg:
            print("** instance id missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command to delete an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """All command to print string representations of all instances."""
        obj_dict = storage.all()
        if not arg:
            print([str(obj) for obj in obj_dict.values()])
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in obj_dict.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Update command to update an instance."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in {"BaseModel", "User"}:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"
        if key not in obj_dict:
            print("** no instance found **")
            return
        setattr(obj_dict[key], args[2], args[3])
        obj_dict[key].save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
