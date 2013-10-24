#module.py -- Silas Nordgren

#Required for running programs.
import os

#The list of extension path strings.
extensions = []

def excludeExt(path):
    #Removes the extension path from wherever it is within the list.
    extensions.remove(path)

def includeExt(path):
    #Adds the extension path to the last spot in the list.
    extensions.append(path)

def poll(command):
    #Iterates through the list of extensions and executes them with the argument supplied with the poll parameter.
    for iterations in len(extensions):
        #Executes the path in the current iteration.
        os.system(extensions + command)
