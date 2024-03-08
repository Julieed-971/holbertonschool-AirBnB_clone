#!/usr/bin/python3
"""
Console module for the HBNB project.
"""

import cmd

from models import storage
from models.engine.file_storage import dict_module


class HBNBCommand(cmd.Cmd):
    """Class for the console module"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        else:
            cls_name = arg.split()[0]

            if cls_name not in dict_module:
                print("** class doesn't exist **")
                pass
            else:
                module = dict_module[cls_name]
                cls_obj = getattr(module, cls_name)
                cls_inst = cls_obj()

                storage.save()
                print(cls_inst.id)

    def do_show(self, arg):
        """Print string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        else:
            args = arg.split()

        if args[0] not in dict_module:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        else:
            cls_name = args[0]
            inst_id = args[1]
            # retrieve the instance from storage with class_name.id
            key = f"{cls_name}.{inst_id}"
            # if instance found, print string representation with __str__
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                new_instance = storage.all()[key]
            print(new_instance)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        else:
            args = arg.split()

        if args[0] not in dict_module:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        else:
            cls_name = args[0]
            inst_id = args[1]
            # retrieve the instance from storage with class_name.id
            key = f"{cls_name}.{inst_id}"
            # if instance found, print string representation with __str__
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                del storage.all()[key]
                storage.save

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        # Find the base case
        cls_name = arg.split()
        if len(cls_name) == 1:
            if cls_name[0] not in dict_module:
                print("** class doesn't exist **")
                return
            else:
                all_string = []
                for arg in storage.all():
                    all_string.append(str(storage.all()[arg]))
                print(all_string)
        else:
            all_string = []
            for arg in storage.all():
                all_string.append(str(storage.all()[arg]))
            print(all_string)

    def do_update(self, arg):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
