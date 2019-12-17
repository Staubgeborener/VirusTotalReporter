# VirusTotalReporter
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/Staubgeborener/VirusTotalReporter/blob/master/LICENSE)

Check files or content of folders with the help of the VirusTotal databases (API) and creates a html report at the end for fast malware analyse    

VirusTotalReporter is compatible with __Python3__.


------------------

## Installation

Clone VirusTotalReporter using `git`:
```sh
git clone https://github.com/Staubgeborener/VirusTotalReporter.git
```

`cd` into the VirusTotalReporter folder:
```sh
cd VirusTotalReporter
```
Install requirements:
```sh
pip install -r requirements.txt
```

------------------

## Usage

`cd` into the VirusTotalReporter folder:
```sh
cd VirusTotalReporter
```
Run the program:
```sh
python VirusTotalReporter
```

Maybe you need root: 
```sh
sudo python VirusTotalReporter
```

### Parameter
```sh
usage: VirusTotalReporter [-h] [-a APIKEY] [-o OUTPUT] [-i INPUT] [-d] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -a APIKEY, --apikey APIKEY
                        API key string
  -o OUTPUT, --output OUTPUT
                        Name of output folder
  -i INPUT, --input INPUT
                        Name of input file OR input folder
  -d, --delay           Activate 15 seconds delay between every examination
  -g, --gui             Start GUI

Example of use: python VirusTotalReporter -a apikey -o ./output -i ./testfile.virus
```


There are two ways to use __VirusTotalReporter__:
### 1. Use GUI

```sh
python VirusTotalReporter -g
```

![VTR_GUI](https://github.com/Staubgeborener/VirusTotalReporter/blob/master/media/VTR_GUI.png)

| Tables              | Explanation                                                  |
| ------------------- |:------------------------------------------------------------:|
| Select File (Input) | Select the file to be checked*                               |
| Select Dir (Input)  | Select the directory with multiples file to be checked*      |
| Output              | Select the output folder                                     |
| API KEY             | Enter your VirusTotal API key. You can click ``[Save]`` to store the key into .virustotal_api_key. In this case, the .virustotal_api_key file will be loaded everytime and you don't have to enter it again and again       |
| Delay               | Checkbox: 15 seconds delay after every API call. Read section "__delay__" for more information |
| Start               | Run the process                                     |

\* either file or directory, but NOT both

The white box further down will give you a small log about the process.


### 2. Use CLI

```sh
python VirusTotalReporter [-a APIKEY] [-o OUTPUT] [-i INPUT] [-d]
```
Example with file: ``python VirusTotalReporter -a 64digitsAPIkey -o ./output-folder -i malware.exe`` \
Example with folder: ``python VirusTotalReporter -a 64digitsAPIkey -o ./output-folder -i ./malware-files``

Note: You have to create the output folder by yourself, VirusTotalReporter will *NOT* create one. Otherwise you get ``FileNotFoundError``.


------------------

### Result
