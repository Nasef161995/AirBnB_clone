#!/usr/bin/python3
"""...."""
import cmd
from models.base_model import BaseModel
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_help(self, arg):
        """..."""
        cmd.Cmd.do_help(self, arg)

    def do_EOF(self, line):
        """...."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    def do_create(self, arg):
        """......."""
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
        """......"""
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
        """......"""
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
        """....."""
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
