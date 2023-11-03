#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    # Create new instance of a class
    def do_create(self, arg):
        """Create a new instance of a class and print its ID"""
        args = arg.split()
        if not args:
            print("Missing class name: create <class_name>")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print(f"Class '{class_name}' doesn't exist")
            return

        new_instance = storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    # Show details of an instance
    def do_show(self, arg):
        """Show instance details: show <class_name> <instance_id>"""
        args = arg.split()
        if not args or len(args) < 2:
            print("Usage: show <class_name> <instance_id>")
            return

        class_name = args[0]
        obj_id = args[1]

        if class_name not in storage.classes():
            print(f"Class '{class_name}' doesn't exist")
            return

        key = class_name + "." + obj_id
        if key not in storage.all():
            print("No instance found")
            return

        print(storage.all()[key])

    # Delete an instance
    def do_destroy(self, arg):
        """Delete an instance: destroy <class_name> <instance_id>"""
        args = arg.split()
        if not args or len(args) < 2:
            print("Usage: destroy <class_name> <instance_id>")
            return

        class_name = args[0]
        obj_id = args[1]

        if class_name not in storage.classes():
            print(f"Class '{class_name}' doesn't exist")
            return

        key = class_name + "." + obj_id
        if key not in storage.all():
            print("No instance found")
            return

        del storage.all()[key]
        storage.save()

    # List all instances or by class
    def do_all(self, arg):
        """List instances: all or all <class_name>"""
        args = arg.split()
        if args and args[0] not in storage.classes():
            print(f"Class '{args[0]}' doesn't exist")
            return

        if args:
            objs = [str(obj) for obj in storage.all().values() if args[0] == obj.__class__.__name__]
        else:
            objs = [str(obj) for obj in storage.all().values()]

        print(objs)

    # Update an instance's attribute
    def do_update(self, arg):
        """Update instance attribute: update <class_name> <instance_id> <attribute_name> <attribute_value>"""
        args = arg.split()
        if not args or len(args) < 4:
            print("Usage: update <class_name> <instance_id> <attribute_name> <attribute_value>")
            return

        class_name = args[0]
        obj_id = args[1]
        attr_name = args[2]

        if class_name not in storage.classes():
            print(f"Class '{class_name}' doesn't exist")
            return

        key = class_name + "." + obj_id
        if key not in storage.all():
            print("No instance found")
            return

        if len(args) < 4:
            print("Attribute value missing")
            return

        attr_value = ' '.join(args[3:])

        # Check and convert the type of the value if needed
        if hasattr(storage.classes()[class_name], attr_name):
            attr_type = type(getattr(storage.classes()[class_name](), attr_name))
            if attr_type is str:
                attr_value = str(attr_value)
            elif attr_type is int:
                attr_value = int(attr_value)
            elif attr_type is float:
                attr_value = float(attr_value)

            setattr(storage.all()[key], attr_name, attr_value)
            storage.all()[key].save()

    def emptyline(self):
        """Handle empty line input"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
