# LaunchEnv
v0.0.2

## About
Command line application created in python to execute your programs or scripts in one command.<br>
Creates launch file with executables and scripts to run them in a single command.
- Note : Not tested for linux. 
- PATH for data storage is given in /launch/utils/utils.py 

## Installation
From PyPI
```
pip install launchenv
```
- For linux
```
sudo pip3 install launchenv
```

From github
```
# Clone project
git clone https://github.com/a-tharva/LaunchEnv && cd LaunchEnv

# Installation
python3 setup.py install

# Run setup
launch
```
## Use
```
>launch -build <workspace_name>
  
>launch -a <workspace_name>
Enter name of program to add this environment: foo
Enter path of program executable: "D:\foo\foo.exe"   or   Drag exe to window the path will appear
  
>launch -env <workspace_name>
```

## Usage
```
 _                           _     _____
| |    __ _ _   _ _ __   ___| |__ | ____|_ ____   __
| |   / _` | | | | '_ \ / __| '_ \|  _| | '_ \ \ / /
| |__| (_| | |_| | | | | (__| | | | |___| | | \ V /
|_____\__,_|\__,_|_| |_|\___|_| |_|_____|_| |_|\_/

launch [-h] [-build] [-a] [-s] [-remove] [-purge] [-env] [-ls]

Run environment

optional arguments:
  -h, --help           show this help message and exit
  -build , --build     Create new work environment/workspace
  -a , --add           Add program to existing work environment
  -s , --show          Show all program in given work environment
  -remove , --remove   Remove program from given work environment
  -purge , --purge     delete the work environment file
  -env , --env         Run environment
  -ls, --list          List all available work environments
```

## Development
Still working on this project.<br>
- The Script functionality is currently not provided as it creates some issues, will add that in future.<br>
- Next version will ask path to store the launch data.<br> 
<!-- -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request


## License
Distributed under the MIT License. [License](https://github.com/a-tharva/LaunchEnv/blob/master/LICENSE)
