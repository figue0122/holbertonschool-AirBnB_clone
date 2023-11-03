#!/usr/bin/python3
"""This module contains the entry point command interpreter."""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quits the console."""
        return True

    def help_quit(self):
        """Displays the help documentation for the 'quit' command."""
        print("Quit command to exit the program")

    def do_EOF(self, args):
        """Handles the EOF command."""
        return True

    def help_EOF(self):
        """Displays the help documentation for the 'EOF' command."""
        print("EOF command to exit the program")

    def emptyline(self):
        """Does nothing when receiving an empty line followed by ENTER."""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it to JSON file and prints the id."""
        # if para chequiar si uso el command solo
        if not args:
            print("** class name missing **")
            return
        # if para chequiar si lo que esta creando ya existe
        args_list = args.split()
        if args_list[0] not in FileStorage.CLASS_DICT:
            print("** class doesn't exist **")
            return
        instance = FileStorage.CLASS_DICT[args_list[0]]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = args.split()
        class_name = args[0] if args else None
        instance_id = args[1] if len(args) > 1 else None
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in FileStorage.CLASS_DICT:
            print("** class doesn't exist **")
            return
        if instance_id is None:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return
        print(storage._FileStorage__objects[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        args = args.split()
        class_name = args[0] if args else None
        instance_id = args[1] if len(args) > 1 else None
        # Checking if class name is provided
        if class_name is None:
            print("** class name missing **")
            return
        # Checking if class name exists in our CLASS_DICT
        if class_name not in FileStorage.CLASS_DICT:
            print("** class doesn't exist **")
            return
        # Checking if instance id is provided
        if instance_id is None:
            print("** instance id missing **")
            return
        # Check if the instance with the given id exists
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return
        # If all checks pass, delete the instance and save changes
        del storage._FileStorage__objects[key]
        FileStorage().save()

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name."""
        args = args.split()
        class_name = args[0] if args else None
        objs_to_print = []
        # If class name is provided but it doesn't exist in our CLASS_DICT
        if class_name and class_name not in FileStorage.CLASS_DICT:
            print("** class doesn't exist **")
            return
        # Loop through all stored objects
        for key, value in storage._FileStorage__objects.items():
            if not class_name or key.split(".")[0] == class_name:
                objs_to_print.append(str(value))
        print(objs_to_print)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if args_list[0] not in FileStorage.CLASS_DICT:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return
        setattr(storage.all()[key], args_list[2], args_list[3].strip("\""))
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
