from lib.interface import *
from lib.file import *
from time import sleep

file = 'report_list.txt'

if not fileExists(file):
    createFile(file)

while True:
    answer = menu(['Existent Records', 'New Record', 'Exit'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        kop('\033[34mADD NEW RECORD\033[m')
        name = str(input('Name: '))
        age = readInt('Age: ')
        report(file, name, age)
    elif answer == 3:
        kop('\033[34mSYSTEM IS EXITING...\033[m')
        sleep(2)
        break
    else:
        print(f'\033[31mERROR! Type a valid option!\033[m')
    sleep(2)

