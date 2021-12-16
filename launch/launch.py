import argparse
import os
import subprocess
import json
from environment.environment import *
from utils.utils import border_msg, logo

CURRENT_PATH = os.path.abspath(__file__)    
CURRENT_PATH = os.path.split(CURRENT_PATH)[0]    
#PATH = 'data\'
    
def initalise(create=None, add=None, show_list=None, delete=None, remove=None, env=None):
    
#    border_msg('    LaunchEnv    ')
    logo()
    
    # Create new work environment
    if create:
        filename = f'{CURRENT_PATH}\data\{create}'
        print(filename)
        create_json(filename)
    
    # Add program to existing work environment
    if add:
        filename = f'{CURRENT_PATH}\data\{add}'
        program = input('Which program to add this environment: ')
        add_json(filename, program)
        
    # Show all programs in the environment
    if show_list:
        filename = f'{CURRENT_PATH}\data\{show_list}'
        read_json(filename)
        
    # Delete program from given environment
    if delete:
        filename = f'{CURRENT_PATH}\data\{delete}'
        item = input('Enter program name to delete from environment: ')
        remove_element_json(filename, item)
        
    # Remove the work environment
    if remove:
        filename = f'{CURRENT_PATH}\data\{remove}' + '.json'
        if os.path.exists(filename):
            verify = input(f'Confirm to delete {remove} environment [y/n]: ')
            if verify == 'y':
                os.remove(filename)
        else:
            print(f'No environment named {remove}.')
    
    # Run environment
    if env:
        filename = f'{CURRENT_PATH}\data\{env}'
        lst = read_json(filename)
        
        print(f'Launching workspace - {env}')
        for _ in lst:
            subprocess.Popen(_)
            print(f'Executed {_}')
        
        
def main():
    # Parser arguments
    parser = argparse.ArgumentParser(description='Run environment')
    parser.add_argument('-c', '--create', help='Create new work environment', 
                        type=str, metavar='')
    parser.add_argument('-a', '--add', help='Add program to existing work environment', 
                        type=str, metavar='')
    parser.add_argument('-s', '--show', help='Show all program in given work environment', 
                        type=str, metavar='')
    parser.add_argument('-delete', '--delete', help='Remove program from given work environment', 
                        type=str, metavar='')
    parser.add_argument('-remove', '--remove', help='Remove the work environment', 
                        type=str, metavar='')
    parser.add_argument('-env', '--env', help='Run environment', 
                        type=str, metavar='')
    args = parser.parse_args()
    
    initalise(create=args.create, add=args.add, 
              show_list=args.show, delete=args.delete, 
              remove=args.remove, env=args.env)
    
    
if __name__ == '__main__':
    main()
#    print(CURRENT_PATH)
#    print('CURRENT')
