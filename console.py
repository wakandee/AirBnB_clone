#!/usr/bin/python3
"""Command line interpreter for Airbnb project."""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def emptyline(self):
        """Empty line doesn't do anything."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to JSON file and print the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + '.' + args[1]
        if obj_key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[obj_key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + '.' + args[1]
        if obj_key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[obj_key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        objs = storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs])
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        print([str(objs[obj]) for obj in objs if args[0] in obj])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = args[0] + '.' + args[1]
        if obj_key not in storage.all():
            print("** no instance found **")
        else:
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            obj = storage.all()[obj_key]
            setattr(obj, args[2], args[3])
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
