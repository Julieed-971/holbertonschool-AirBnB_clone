#!/usr/bin/python3
"""
Console module for the HBNB project.
"""

import cmd
import os
import json
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
            cls_name = arg.split()

        if cls_name[0] not in dict_module:
            print("** class doesn't exist **")
            return

        if len(cls_name) < 2:
            print("** instance id missing **")
            return

        else:
            cls_name = cls_name[0]
            inst_id = cls_name[1]
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
            cls_name = arg.split()

        if cls_name[0] not in dict_module:
            print("** class doesn't exist **")
            return

        if len(cls_name) < 2:
            print("** instance id missing **")
            return

        else:
            cls_name = cls_name[0]
            inst_id = cls_name[1]
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
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        if os.path.exists("file.json"):
            with open("file.json", "r") as f:
                loaded_storage = json.load(f)

        arg_name = arg.split()

        if len(arg_name) == 0:
            print("** class name missing **")
            return
        if len(arg_name) == 1:
            if arg_name[0] not in dict_module:
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        if len(arg_name) == 2:
            key = f"{arg_name[0]}.{arg_name[1]}"
            if key not in loaded_storage:
                print("** no instance found **")
                return
            else:
                print("** attribute name missing **")
                return
        if len(arg_name) == 3:
            print("** value missing **")
            return
        else:
            cls_name = arg_name[0]
            inst_id = arg_name[1]
            inst_attr = arg_name[2]
            inst_attr_value = arg_name[3]

            key = f"{cls_name}.{inst_id}"

            if key in loaded_storage:
                attribute_dict = loaded_storage[key]
                if inst_attr in attribute_dict:
                    attribute_dict[inst_attr] = inst_attr_value
                else:
                    attribute_dict[inst_attr] = inst_attr_value
                    storage.save

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
