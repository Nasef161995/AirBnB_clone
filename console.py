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

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

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
        
    def do_update(self, arg):
        """command Updates an instance based on the class name and id"""

        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
