# LaunchEnv
v0.0.4

## About
Command line application created in python to execute your programs or scripts in one command. <br> 
Launch your work/misc environment with just one command.<br>
Programs and commands are stoerd in json launch file.
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
>launch -build <environment_name>
  
>launch -a <environment_name>
Enter name of program to add this environment: foo
Enter path of program executable: "D:\foo\foo.exe"   or   Drag exe to window the path will appear

For script -
>launch -a <environment_name>
Enter name of program to add this environment: foo
Enter path of program executable: python "D:\foo\foo.py"   or   python Drag exe to window the path will appear
  
  script with output
  windows - 
    : start cmd /K python 'D:\foo\foo.py'
  linux - 
    : 
  
For advance use -
>launch -a <environment_name>
Enter name of program to add this environment: opera incognito
Enter path of program executable: "D:\foo\opera.exe" -incognito  or   Drag exe to window the path will appear -incognito
  
>launch -run <environment_name>
```

## Usage
```
 _                           _     _____
| |    __ _ _   _ _ __   ___| |__ | ____|_ ____   __
| |   / _` | | | | '_ \ / __| '_ \|  _| | '_ \ \ / /
| |__| (_| | |_| | | | | (__| | | | |___| | | \ V /
|_____\__,_|\__,_|_| |_|\___|_| |_|_____|_| |_|\_/

usage: launch [-h] [-build] [-a] [-sh] [-t] [-e] [-remove] [-run] [-ls]
              [-purge]

Run environment

optional arguments:
  -h, --help           show this help message and exit
  -build , --build     Create new work environment/launch file
  -a , --add           Add program to existing launch file
  -sh , --show         Show all program in launch file
  -t , --time          Time in seconds between execution
  -e , --exclude       Run program except
  -remove , --remove   Remove program from given launch file
  -run , --run         Run environment
  -ls, --list          List all available launch file
  -purge , --purge     delete the work launch file
```

## Development
Still working on this project.<br>
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
