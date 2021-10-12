from lib.interface import *

def fileExists(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Error creating file!')
    else:
        print(f'File {name} created successfuly!')


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('\033[31mERROR reading file!\033[m')
    else:
        kop('\033[34mREPORTED\033[m')
        for lines in a:
            data = lines.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years old')

    finally:
        a.close()

def report(file, name='unknown', age=0):
    try:
        a = open(file, 'at')
    except:
        print('\033[31mERROR opening file!\033[m')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('\033[31mERROR writing data!\033[m')
        else:
            print(f'New record of {name} added!')
            a.close()
