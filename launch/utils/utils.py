from datetime import datetime
from sys import platform


def border_msg(msg):
    # For message box
    row = len(msg)
    h = ''.join(['+'] + ['-' * row] + ['+'])
    result = h + '\n'"|"+msg+"|"'\n' + h
    print(result)


def PATH():
    # To check current system
    if platform == 'win32':
        path = 'C:\\.launchfiles'
    elif platform == 'linux':
        path = '/home/.launchfiles'
    else:
        path = 'C:\\.launchfiles'

    return path


def log(msg: str) -> None:
    f = open(f'{PATH()}/log.txt', 'a+')
    f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}: {msg}\n')
    f.close()


def logo():
    # Menu logo
    print('''   
 _                           _     _____
| |    __ _ _   _ _ __   ___| |__ | ____|_ ____   __
| |   / _` | | | | '_ \ / __| '_ \|  _| | '_ \ \ / /
| |__| (_| | |_| | | | | (__| | | | |___| | | \ V /
|_____\__,_|\__,_|_| |_|\___|_| |_|_____|_| |_|\_/
V0.0.5
''')
