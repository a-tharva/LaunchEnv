import json


class data:
    """Logic for launch file data """

    def read_(filename):
        # Read json and return dictionary
        with open(filename + '.json', 'r') as f:
            dic = json.load(f)
            return dic

    def create_(filename):
        # create json file
        dic = {}
        with open(filename + '.json', 'a+') as f:
            json.dump(dic, f)

    def add_(filename, key, value):
        # Add program to json file
        with open(filename + '.json', 'r+') as f:
            dic = json.load(f)
            dic = dic.copy()
            dic.update({key: value})
            f.seek(0)
            json.dump(dic, f, indent=2)
            print(f'Program {key} added to launch file')

    def remove_element_(filename, item_key):
        # Remove program from json file
        with open(filename + '.json') as f:
            dic = json.load(f)
            dic = dic.copy()
            if item_key not in dic:
                print(f'Program {item_key} not found')
                return
            del dic[item_key]
            print('Program removed')

        with open(filename + '.json', 'w') as f:
            json.dump(dic, f)
