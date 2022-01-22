import os
import argparse
import subprocess

import launch.environment.environment as lee
from launch.utils.utils import PATH, border_msg, logo


CURRENT_PATH = PATH

# Initalise function to call other functions based on arguments
def initalise(build=None, add=None, show_list=None, delete=None, remove=None, env=None):
    
    # Create new work environment
    if build:
        logo()
        print(f'Launch file with name {build} will be created...')
        filename = f'{CURRENT_PATH}\{build}'
        lee.create_json(filename)
    
    # Add program to existing work environment
    if add:
        filename = f'{CURRENT_PATH}\{add}'
        program = input('Which program to add this environment: ')
        try:
            lee.add_json(filename, program)
        except Exception as Error:
            print(Error)
        
    # Show all programs in the environment
    if show_list:
        filename = f'{CURRENT_PATH}\{show_list}'
        lst = lee.read_json(filename)
        print(f'Workspace {show_list}')
        for i in lst:
            print(i)
        
    # Delete program from given environment
    if delete:
        filename = f'{CURRENT_PATH}\{delete}'
        item = input('Enter program name to delete from environment: ')
        lee.remove_element_json(filename, item)
        
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
        try:
            lst = lee.read_json(filename)
            print(f'Launching workspace - {env}')
            for _ in lst:
                subprocess.Popen(_)
                print(f'Executed {_}')
        except FileNotFoundError:
            print(f'No Workspace named {env} found')
            print('Here is list of available workspace:')
            for _ in os.listdir(CURRENT_PATH):
                if _.endswith('.json'):
                    print(' ',_.replace('.json',''))
        
        
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