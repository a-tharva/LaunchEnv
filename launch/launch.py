import argparse
import os
import subprocess
import json

from launch.environment.environment import *
from launch.utils.utils import PATH, border_msg, logo


#CURRENT_PATH = os.path.abspath(__file__)    
#CURRENT_PATH = os.path.split(CURRENT_PATH)[0]    
#PATH = 'data\'

CURRENT_PATH = PATH
    
def initalise(build=None, add=None, show_list=None, delete=None, remove=None, env=None):
    
    # Create new work environment
    if build:
        logo()
        print(f'Launch file with name {build} will be created...')
        filename = f'{CURRENT_PATH}\{build}'
        create_json(filename)
    
    # Add program to existing work environment
    if add:
        filename = f'{CURRENT_PATH}\{add}'
        program = input('Which program to add this environment: ')
        try:
            add_json(filename, program)
        except Exception as Error:
            print(Error)
        
    # Show all programs in the environment
    if show_list:
        filename = f'{CURRENT_PATH}\{show_list}'
        lst = read_json(filename)
        print(f'Workspace {show_list}')
        for i in lst:
            print(i)
        
    # Delete program from given environment
    if delete:
        filename = f'{CURRENT_PATH}\{delete}'
        item = input('Enter program name to delete from environment: ')
        remove_element_json(filename, item)
        
    # Remove the work environment
    if remove:
        filename = f'{CURRENT_PATH}\{remove}' + '.json'
        if os.path.exists(filename):
            verify = input(f'Confirm to delete {remove} environment [y/n]: ')
            if verify == 'y':
                os.remove(filename)
        else:
            print(f'No environment named {remove}.')
    
    # Run environment
    if env:
        logo()
        filename = f'{CURRENT_PATH}\{env}'
        lst = read_json(filename)
        
        print(f'Launching workspace - {env}')
        for _ in lst:
            subprocess.Popen(_)
            print(f'Executed {_}')
        
        
def main():
    # Parser arguments
    parser = argparse.ArgumentParser(description='Run environment')
    parser.add_argument('-build', '--build', help='Create new work environment/workspace', 
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
    
    initalise(build=args.build, add=args.add, 
              show_list=args.show, delete=args.delete, 
              remove=args.remove, env=args.env)
    
    
if __name__ == '__main__':
    main()