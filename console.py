#!/usr/bin/python3
"""Module of cmd interpreter
"""

import cmd
from models.base_model import BaseModel
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """class for console"""

    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """command to exit the program"""

        return True

    def do_help(self, arg):
        """ help command to print the comment"""

        cmd.Cmd.do_help(self, arg)

    def do_EOF(self, line):
        """command to exit the program"""

        return True

    def emptyline(self):
        """Do nothing on an empty line."""

        pass

    def do_create(self, arg):
        """command create a new instance and save"""

        if arg:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                new_instance = eval(f"{arg}()")
                new_instance.save()
                print(new_instance.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """command show the string representation \
            of all instances"""

        if arg:
            list_arg = arg.split()

            if list_arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(list_arg) == 1:
                print("** instance id missing **")
            else:
                mydict = storage.all()
                name = f"{list_arg[0]}.{list_arg[1]}"
                if name in mydict:
                    print(mydict[name])
                else:
                    print("** no instance found **")

        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """command deletes instances according name and id """

        if arg:
            list_arg = arg.split()

            if list_arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(list_arg) == 1:
                print("** instance id missing **")
            else:
                mydict = storage.all()
                name = f"{list_arg[0]}.{list_arg[1]}"
                if name in mydict:
                    del mydict[name]
                    storage.save()
                else:
                    print("** no instance found **")

        else:
            print("** class name missing **")

    def do_all(self, arg):
        """command prints all string representation \
            of all instances"""

        mydict = storage.all()
        mylist = []
        for i in mydict.values():
            mylist.append(str(i))
        if arg:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                newlist = []
                for key, value in mydict.items():
                    if arg in key:
                        newlist.append(str(value))
                print(newlist)
        else:
            print(mylist)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
