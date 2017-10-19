# UNITE Ground Support Software

UNITE Ground Support Software is used by the UNITE CubeSat team from the University of Southern Indiana to collect instrument data and present it in a readable format. 

The testing version of the software is used to collect data through the 3U CubeSat's diagnostic port and is run via a Raspberry Pi 3 Model B and two Arduinos (Mega 2560). 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:


This software has only been tested on a [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) running Ubuntu MATE 16.04.2 (Xenial):

https://ubuntu-mate.org/download/


You will need to install the Adruino IDE editor 1.8.4 (Linux ARM):

https://www.arduino.cc/en/Main/OldSoftwareReleases


### Installing

You can install this software using git:

First, clone the repository into your desired directory
```
$cd /fill_your_directory_path_here
$git clone https://github.com/UNITE-CubeSat/UNITEGroundSupportSoftware.git
```

Next, give the software permission to execute
```
$sudo chmod +x UNITEGroundSupportSoftware/run.sh
```

Last, run the software by executing run.sh
```
$sudo ./UNITEGroundSupportSoftware/run.sh
```

## Running the tests

After starting the script, follow these steps:

1. Make sure that each Arduino is plugged into the RPi 3.
   The default ports are __/dev/ttyACM0__ and __/dev/ttyACM1__ but can be altered in the run.sh script and the __*Logger.py__ files.

2. The startup script will ask you for the working directory which will just be the repository directory.

```bash
Starting Ground Test Software

Please drag your testing directory into the terminal and press enter

# Drag the UNITEGroundSupportSoftware folder below
{/path_to_directory/}
``` 

3. Make a backup. If you have run the script before, it will ask if you want to backup the current data to a timestamped folder.

```bash
# Enter 'y' if you want to make a backup or 'n' if you want to overwrite the current data logs
Would you like to save a backup of the current $LOGDIR directory? (y/n)
```

4. Give each Arduino permission to read from the USB Serial Port.

```bash
Update Arduino permissions...

[username]: {password_here}
```

5. Program each Arduino with its corresponding Arduino script found in the Arduino subdirectory.

```bash
# Program the Arduino on port PORT_NAME with ARDUINO_SCRIPT using the ARDUINO IDE
# If it has been programmed, enter y and continue
Has Arduino on port {PORT_NAME} been programmed with '{ARDUINO_SCRIPT}' ? (y/n)
```

6. Give both python logging scripts permission to run

```bash
# Two different terminal windows will pop up asking for login password
[username]: {password_here}
```

Each window will display what logger file has started.

Either

```
Raspberry Pi Transmission Logger started...
```

or

```
Diagnostic Logger started...
```

The end result of the run.sh script will have two terminal windows open that will print out any data that comes through the Arduinos from the satellite.

## Contributing

Not currently accepting pull requests.

## Authors

* **Zack Snyder** - *Initial work*

* **Colin Runnion** - *Parsing Scripts*

See also the list of [contributors](https://github.com/UNITE-CubeSat/UNITEGroundSupportSoftware/contributors) who participated in this project.

## Acknowledgments

* NASA USIP - for making this project possible
* INSGC - for handling funding
* USI - for incredible support throughout the whole project
