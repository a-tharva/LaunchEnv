import os
import argparse
from .launch import handle
from .utils.utils import PATH


CURRENT_PATH = PATH()


def initalise(build=None, add=False, show_list=None, time=None, exc=None, remove=None, env=None, ls=False, purge=None):
    # Initalise function to call other functions based on arguments
    
    if build:
        # Create new launch file
        filename = f'{CURRENT_PATH}\{build}'
        handle.build(filename, build)
    
    if add:
        # Add program to existing launch file
        filename = f'{CURRENT_PATH}\{add}'
        handle.add(filename)
    
    if show_list:
        # Show all programs in the launch file
        filename = f'{CURRENT_PATH}\{show_list}'
        handle.show_lst(filename, show_list)
    
    if remove:
        # Delete program from given launch file
        filename = f'{CURRENT_PATH}\{remove}'
        handle.remove_element(filename)
    
    if env:
        # Run environment
        filename = f'{CURRENT_PATH}\{env}'
        handle.launch(filename, env, time, exc)
    
    if ls:
        # List all availabel work environments
        handle.ls()
    
    if purge:
        # Remove the work environment
        filename = f'{CURRENT_PATH}\{purge}' + '.json'
        handle.purge(filename, purge)
    
    
def main():
    # Parser arguments
    parser = argparse.ArgumentParser(description='Run environment')
    parser.add_argument('-build', '--build', help='Create new work environment/launch file', type=str, metavar='')
    
    parser.add_argument('-a', '--add', help='Add program to existing launch file', type=str, metavar='')
    
    parser.add_argument('-sh', '--show', help='Show all program in launch file', type=str, metavar='')
    
    parser.add_argument('-t', '--time', help='Time in seconds between execution', type=int, metavar='')
    
    parser.add_argument('-e', '--exclude', help='Run program except', type=str, metavar='')
    
    parser.add_argument('-remove', '--remove', help='Remove program from given launch file', type=str, metavar='')
    
    parser.add_argument('-run', '--run', help='Run environment', type=str, metavar='')
    
    parser.add_argument('-ls', '--list', help='List all available launch file', action='store_true')
    
    parser.add_argument('-purge', '--purge', help='delete the work launch file', type=str, metavar='')
    
    args = parser.parse_args()
    
    initalise(build=args.build, 
              add=args.add, 
              show_list=args.show, 
              time=args.time,
              exc=args.exclude,
              remove=args.remove, 
              env=args.run, 
              ls=args.list,
              purge=args.purge) 
    
    
if __name__ == '__main__':
    main()