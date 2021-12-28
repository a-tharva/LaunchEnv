import os
import json


# Read json and return list
def read_json(filename):
    lst = []
    with open (filename + '.json', 'r') as f:
        lst = json.load(f)
        return lst
#        for i in lst:
#            print(i)

# create json file
def create_json(filename):
    if os.path.exists(f'{filename}.json'):
        print('File already exist.')
    else:
        lst = []
        with open(filename + '.json', 'a+') as f:
            json.dump(lst, f)
        
# Add program to json file list
def add_json(filename, program):
    lst = []
    with open (filename + '.json', 'r+') as f:
        lst = json.load(f)
        lst = lst.copy()
        lst.append(program)
        f.seek(0)
        json.dump(lst, f)

# Remove program from json file list
def remove_element_json(filename, item):
    lst = []
    with open (filename + '.json') as f:
        lst = json.load(f)
        lst = lst.copy()
        
        # Search for program in the list
        l = [i for i in lst if item in i]
        # Generator object is created 
        # Traversing 
        indx = None
        for s in l:
            indx = lst.index(s)
            print(indx)
        lst.remove(lst[indx])
        
    with open (filename + '.json', 'w') as f:
        json.dump(lst, f)
    
    
# Delete json file
def delete_json(filename):
    if os.path.exixts(f'{filename}.json'):
        os.remove(f'{filename}.json')
    else:
        print('No such file exist.')
        
#lst = read_json('data')
#for _ in lst:
#    print(_)