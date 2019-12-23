# VirusTotalReporter
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/Staubgeborener/VirusTotalReporter/blob/master/LICENSE)

Check files or content of folders with the help of the VirusTotal databases (API) and creates a html report at the end for fast malware analysis    

VirusTotalReporter is compatible with __Python3__.

You can get your [VirusTotal Public API Key for free](https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key).

------------------

## Installation
### git (Windows, Linux, macOS)
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

### Download Windows executable
There is also a [windows compiled executable](https://staubgeborener.de/virustotalreporter/) (should work on any windows version, wether 32 bit or 64 bit). \
__Note__: This is only the GUI, for instructions look at the section [1. Use GUI](https://github.com/Staubgeborener/VirusTotalReporter#1-use-gui).

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
(If you have downloaded the executable Windows file, simply double-click the .exe file) 

![VTR_GUI](https://github.com/Staubgeborener/VirusTotalReporter/blob/master/media/VTR_GUI.png)

| Tables              | Explanation                                                  |
| ------------------- |:------------------------------------------------------------:|
| Select File (Input) | Select the file to be checked*                               |
| Select Dir (Input)  | Select the directory with multiples file to be checked*      |
| Output              | Select the output folder                                     |
| API KEY             | Enter your VirusTotal API key. You can click ``[Save]`` to store the key into .virustotal_api_key. In this case, the .virustotal_api_key file will be loaded everytime and you don't have to enter it again and again       |
| Delay               | Checkbox: 15 seconds delay after every API call. Read section [delay](https://github.com/Staubgeborener/VirusTotalReporter#delay) for more information |
| Start               | Run the process                                     |

\* either file or directory, but NOT both

The white box further down will give you a small log about the process.


### 2. Use CLI

```sh
python VirusTotalReporter [-a APIKEY] [-o OUTPUT] [-i INPUT] [-d]
```
Example with file: ``python VirusTotalReporter -a 64digitsAPIkey -o ./output-folder -i malware.exe`` \
Example with folder: ``python VirusTotalReporter -a 64digitsAPIkey -o ./output-folder -i ./malware-files -d``

Note: You have to create the output folder by yourself, VirusTotalReporter will *NOT* create one. Otherwise you get ``FileNotFoundError``.

#### Delay

In addition: The public API Key is limited to [4 requests per minute](https://developers.virustotal.com/reference#getting-started). That means, if you do more tha 4 requests per minute (i.e. you check a folder with 5 or more files) you will get the API response code 204: "Request rate limit exceeded. You are making more requests than allowed. You have exceeded one of your quotas (minute, daily or monthly). Daily quotas are reset every day at 00:00 UTC.".
In this case, just use the parameter ``-d`` (CLI) or check the box "Delay" (GUI). After each request, the program will wait 15 seconds until the next request. This makes it possible to check automatically multiple files without getting a response code 204.

------------------

### Result

At the end, an html report (in the format "report_unix-epoch-timestamp.html e.g. report_1577093977.html) is created in the specified output folder. This contains a summary of the previous analysis. Each individual report is located in the output folder in a newly created "reports"-directory.

Important: The html report needs the individual reports in the report folder. E.g. if the html report is copied, the reports folder with the individual files must also be in the same directory.

![VTR_GUI](https://github.com/Staubgeborener/VirusTotalReporter/blob/master/media/VTR_Result.png)

To get a first overview, the files are sorted according to their evaluation in the colors "green" (probably no malware, < 10%\*), "orange" (maybe malware, between 10% and 33%\*) and "red" (quite likely malware, > 33%\*) in the left column. Detailed information can be found in the right column. This can be changed in the file [.vt.py at line 161](https://github.com/Staubgeborener/VirusTotalReporter/blob/master/VirusTotalReporter/vt.py#L161)

\* based on a percentage calculation of positive analysis against overall analysis

------------------

### Still todo
* beautify GUI
* clean up code
* add Private API support 
