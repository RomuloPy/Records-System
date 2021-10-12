def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! Please type a int digit.\033[m')
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUser chose to don't type that number")
            return 0
        else:
            return n

def line(size = 42):
    return '-' * size


def kop(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(list):
    kop('Main Menu')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opc = readInt('\033[32mYour option: \033[m')
    return opc
