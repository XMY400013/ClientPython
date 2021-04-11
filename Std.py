import sys 
from io import StringIO

class StdOut:
    def __init__(self):
        self.__stdout = ''


    def write(self, text):
        self.__stdout+= text
    

    def read(self):
        return self.__stdout.strip()


#modern !!! add err exception
class StdErr:
    def __init__(self):
        self.__stderr = ''


    def write(self, text):
        self.__stderr+= text
    

    def read(self):
        return self.__stderr.strip()


class Std:

    def __enter__(self):
        self.__stdout = sys.stdout
        sys.stdout = self.__out = StdOut()
        return self

    def __exit__(self, *args):
        sys.stdout = self.__stdout


    @property
    def read(self):
        return self.__out.read()




