import os
import time
import subprocess

from .environment.environment import data
from .utils.utils import PATH, logo

CURRENT_PATH = PATH()

class handle:
    """Logic for launch"""
    
    
    def add(filename):
        # Add to launch file
        name = input('Enter name of program to add this launch file: ')
        path = input('Enter path of program launch file: ')
        try:
            data.add_(filename, name, path)
        except Exception as Error:
            print(Error)
            
            
    def build(filename, build):
        # Build launch file
        print(f'Launch file with name {build} will be created...')
        if os.path.exists(f'{filename}.json'):
            print('File already exist. Try another name')
        else:
            data.create_(filename)
        print(f'Launch file {build} created')
            
            
    def launch(filename, env, sleep_time, exc):
        # launch function
        try:
            dic = data.read_(filename)
            print(f'Launching workspace - {env}')
            logo()
            handle.run(dic, sleep_time, exc)
        except FileNotFoundError:
            print(f'No launch file named {env} found')
            handle.ls()
    
    
    def purge(filename, purge):
        # Delete launch file
        if os.path.exists(filename):
            verify = input(f'Confirm to delete {purge} launch file [y/n]: ')
            if verify == 'y':
                os.remove(filename)
                print(f'Purged {purge} launch file')
        else:
            print(f'No launch file named {purge}.')
    
    
    def remove_element(filename):
        # Remove element from launch file 
        item = input('Enter program name to delete from launch file: ')
        data.remove_element_(filename, item)
    
    
    def show_lst(filename, show_list):
        # List all elements from launch file
        try:
            dic = data.read_(filename)
            print(f'launch file {show_list}')
            for _ in dic:
                print(f' {_}: {dic[_]}')
        except FileNotFoundError:
            print(f'No launch file named {show_list} found')

    
    @staticmethod
    def ls():
        # List all launch environments
        print('Here is list of available launch files:')
        for _ in os.listdir(CURRENT_PATH):
            if _.endswith('.json'):
                print(' ',_.replace('.json',''))
            
    
    @staticmethod                
    def run(dic, sleep_time, exc=''):
        # Run programs from launch file
        sleep_time = 0 if sleep_time is None else sleep_time
        for _ in dic:
            try:
                if exc != _:
                    subprocess.Popen(dic[_], shell=True)
                    print(f'Executed {_}')
                    time.sleep(sleep_time)
            except Exception as Error:
                print(Error)
                print(f'Could not open {_}:{dic[_]}. Check if path/file_name is correct')