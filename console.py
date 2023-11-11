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

    def do_EOF(self, line):
        """command to exit the program"""
       
        return True

    def emptyline(self):
        """Do nothing on an empty line"""

        return False

    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
