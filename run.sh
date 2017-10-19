#!/bin/bash

BASEDIR=""

ARDUINO_PORT_DIAG="ACM0"
ARDUINO_PORT_SIMP="ACM1"

function getWorkingDirectory {	
	echo -e "Please drag your testing directory into the terminal and press enter\n"
	read BASEDIR
	BASEDIR="${BASEDIR%\'}"
	BASEDIR="${BASEDIR#\'}"
	if [[ -d $BASEDIR && -n $BASEDIR ]]; then
		PYTHON=`ls $BASEDIR | grep Logger`
		echo $PYTHON
		if [[ -n $PYTHON ]]; then
			echo -e "\nWorking Directory: $BASEDIR\n"
		else
			echo -e "\nNo Python parsing files found... please choose a different directory\n"
			getWorkingDirectory
		fi
	else
		getWorkingDirectory
	fi
}

function initializeDiagDir {
	LOGDIR="$BASEDIR/Diagnostic_Logs"
	# Check if directory already exists
	if [ -d $LOGDIR ]; then 
		# Diag directory already exists
		echo "Directory $LOGDIR already exists"
		while [[ $REPLY != "y" && $REPLY != "n" ]]; do
			echo -en "\nWould you like to save a backup of the current $LOGDIR directory? (y/n) \c"
			read
			# Create a fresh $LOGDIR with backup
			if [ $REPLY = "y" ]; then
				# Create a new directory with timestamp
				BACKUPDIR="$(date +%H:%M:%S_%m-%d-%Y)"
				mkdir -v $BACKUPDIR
				# Copy contents of log directory into backup directory
				cp -nrv -t $BACKUPDIR $LOGDIR
				# Delete and remake log directory
				rm -rf $LOGDIR
				mkdir $LOGDIR
			else
				# Create a fresh $LOGDIR without backup
				if [ $REPLY = "n" ]; then
					rm -rf $LOGDIR
					mkdir $LOGDIR
				fi
			fi		
		done
	else
		mkdir $LOGDIR
	fi
}

updatePermissionsFor () {
	# Select tty port
	PORT="/dev/tty$1"
	echo $PORT
	# If port exists
	if [ -e $PORT ]; then
		# Give port permission to program and to receive data
		sudo chmod 666 $PORT
		echo "Successfully updated permissions for Arduino on port $1..."
	else
		echo -e "ERROR: Arduino not recognized on port '$1'\nPlease check connection and try again..."
		echo "Or update Arduino ports in run.sh file and in python logger files"
		exit 80	
	fi
}

checkIfArduinoIsProgrammed () {
	RESPONSE="z"
	ARDUINO_SCRIPT=""
	# Set ARDUINO_SCRIPT based on Arduino port	
	if [ $1 = $ARDUINO_PORT_SIMP ]; then
		ARDUINO_SCRIPT="UNITE_Simplex_Data_Save.ino"
	else
		if [ $1 = $ARDUINO_PORT_DIAG ]; then
			ARDUINO_SCRIPT="Diagnostic_Log.ino"
		else
			echo "ERROR: Please update Arduino ports in run.sh file"
			exit 81		
		fi
	fi	
	
	# Ask the user if the Arduino Boards have been programmed properly
	while [[ $RESPONSE != "y" ]]; do
		echo -en "Has Arduino on port $1 been programmed with '$ARDUINO_SCRIPT' ? (y/n) \c"
		read RESPONSE
		if [[ $RESPONSE = "y" ]]; then
			break
		else
			echo "Please program Arduino on port $1 before proceeding..."
		fi
	done
} 

echo -e "\nStarting Ground Test Software\n"

getWorkingDirectory

echo -e "\nInitializing Filesystem...\n"

initializeDiagDir

echo -e "\nUpdate Arduino permissions...\n"

updatePermissionsFor $ARDUINO_PORT_DIAG
updatePermissionsFor $ARDUINO_PORT_SIMP

echo -e "\nReminder to program Arduinos...\n"

checkIfArduinoIsProgrammed $ARDUINO_PORT_DIAG
checkIfArduinoIsProgrammed $ARDUINO_PORT_SIMP

echo -e "\nStarting Python parsing scripts...\n"

x-terminal-emulator -e sudo python $BASEDIR/PiArduinoLogger.py
echo "Successfully started PiArduinoLogger.py"

x-terminal-emulator -e sudo python $BASEDIR/DiagnosticLogger.py
echo "Successfully started DiagnosticLogger.py"
