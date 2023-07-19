'''
Write your solution for 6. PIAT: Check Setup here.

Author: Bassam Batch
SID: 310229251
Unikey: bbat2575
'''

import os
import sys
import time
from datetime import datetime
import shutil

# you can make more functions or global read-only variables here if you please!

def logging(logs: list, date: str, time: str) -> None:
    filename = f"/home/logs/{date}/{time}.txt"
    directory = f"/home/logs/{date}"
    
    # Check if logs directory exists; if not, create it
    if not os.path.isdir("/home/logs"):
        os.mkdir("/home/logs")

    # Check today's log directory exists; if not, create it
    if not os.path.isdir(directory):
        os.mkdir(directory)

    # Create log file
    log_file = open(filename, 'w')

    i = 0

    while i < len(logs):
        log_file.write(logs[i] + '\n')
        i += 1

    log_file.close()
    

def verification(master: str, timestamp: str) -> list:
    output = []

    output.append(f"{timestamp} Start verification process.")
    output.append(f"{timestamp} Extracting paths in configuration file.")

    # Retrieve config.txt file ('with' and 'as' keywords ensure file is closed afterwards)
    config_file = master + 'config.txt'

    with open(config_file) as conf:
        conf = conf.readlines()
    
    # Retrive three lists:
    # - mk_dirs = contains the directories from config.txt that need to be made (e.g. /home/files/)
    # - mk_files = contains the files from config.txt that need to be made (e.g. /home/files/animals.txt)
    # - master_files = contains the files from config.txt with absolute path to master directory (e.g. /home/master/files/animals.txt)
    mk_dirs, mk_files, master_files = analyse_conf(conf, master)

    total_dirs = len(mk_dirs)
    total_files = len(mk_files)

    output.append(f"Total directories to check: {total_dirs}")
    output.append(f"{timestamp} Checking if directories exists.")

    # Check if directories exist, if not, notify user
    i = 0
    while i < total_dirs:
        if os.path.isdir(mk_dirs[i]):
            output.append(f"{mk_dirs[i]} is found!")
        else:
            output.append(f"{mk_dirs[i]} NOT found!")
        i += 1

    output.append(f"{timestamp} Extracting files in configuration file.")

    i = 0

    while i < total_files:
        output.append(f"File to check: {mk_files[i]}")
        i += 1

    output.append(f"Total files to check: {i}")
    output.append(f"{timestamp} Checking if files exists.")

    i = 0

    while i < total_files:
        if os.path.isfile(mk_files[i]):
            output.append(f"{mk_files[i]} found!")
        else:
            output.append(f"{mk_files[i]} NOT found!")
        i += 1

    output.append(f"{timestamp} Check contents with master copy.")

    i = 0

    # Compare master files with user files
    while i < total_files:
        if os.path.isfile(mk_files[i]) and os.path.isfile(master_files[i]):
            with open(mk_files[i]) as file1:
                with open(master_files[i]) as file2:                
                    file1_list = file1.readlines()
                    file2_list = file2.readlines()
                    if file1_list == file2_list:
                        output.append(f"{mk_files[i]} is same as {master_files[i]}: True")
                    else:
                        j = 0
                        while j < len(file2_list):
                            # Assign elements to variables for comparison since f-string expressions cannot include backslashes (causes SyntaxError)
                            first = file1_list[j].strip('\n')
                            second = file2_list[j].strip('\n')
                            output.append(f"File name: {mk_files[i]}, {first}, {second}")
                            if file1_list[j] != file2_list[j]:
                                output.append("Abnormalities detected...")
                                return output
                            j += 1
        i += 1

    output.append(f"{timestamp}  Verification complete.")

    return output
   

def installation(master: str, timestamp: str) -> list:
    output = []

    output.append(f"{timestamp} Start installation process.")
    output.append(f"{timestamp} Extracting paths in configuration file.")

    # Retrieve config.txt file ('with' and 'as' keywords ensure file is closed afterwards)
    config_file = master + 'config.txt'

    with open(config_file) as conf:
        conf = conf.readlines()
    
    # Retrive three lists:
    # - mk_dirs = contains the directories from config.txt that need to be made (e.g. /home/files/)
    # - mk_files = contains the files from config.txt that need to be made (e.g. /home/files/animals.txt)
    # - master_files = contains the files from config.txt with absolute path to master directory (e.g. /home/master/files/animals.txt)
    mk_dirs, mk_files, master_files = analyse_conf(conf, master)

    total_dirs = len(mk_dirs)
    total_files = len(mk_files)

    output.append(f"Total directories to create: {total_dirs}")
    output.append(f"{timestamp} Create new directories.")

    # Check if directories exist, if not, create them
    i = 0
    while i < total_dirs:
        if not os.path.isdir(mk_dirs[i]):
            os.mkdir(mk_dirs[i])
            output.append(f"{mk_dirs[i]} is created successfully.")
        else:
            output.append(f"{mk_dirs[i]} exists. Skip directory creation.")      
        i += 1

    output.append(f"{timestamp} Extracting paths of all files in {master}.")

    # Get list of files in master directories and sub-directories
    master_list = list_files(master)

    # Remove config.txt from the list
    master_list.remove(master+'config.txt')

    i = 0

    while i < len(master_list):
        output.append(f"Found: {master_list[i]}")
        i += 1

    output.append(f"{timestamp}  Create new files.")

    i = 0
    
    while i < total_files:
        output.append(f"Creating file: {mk_files[i]}")
        i += 1

    output.append(f"{timestamp} Copying files.")

    i = 0
    
    while i < len(master_files):
        output.append(f"Locating: {master_files[i].split('/')[-1]}")

        if os.path.isfile(master_files[i]):
            output.append(f"Original path: {master_files[i]}")
            output.append(f"Destination path: {mk_files[i]}")
            shutil.copy(master_files[i], mk_files[i])
        else:
            output.append(f"Original path: {master_files[i]} is not found.")
            output.append("Installation error...")
            return output
        i += 1

    output.append(f"{timestamp}  Installation complete.")

    return output


def analyse_conf(conf, master):
    # Count the number of directories to create and store them in a list (mk_dirs)
    # Also create a list of files that need to be created (mk_files)
    i = 0
    mk_dirs = []
    mk_files = []
    master_files = []
    current_dir = master

    while i < len(conf):
        # If element is a directory
        if conf[i][0] == "/":
            mk_dirs.append(conf[i].strip('\n'))
            current_dir = conf[i].strip('\n').strip()
        # Else if it's a file
        else:
            mk_files.append(current_dir+conf[i][2:].strip('\n').strip())
            master_files.append(master+current_dir.strip('/home/')+conf[i][1:].strip('\n').strip())

        i += 1
    
    return mk_dirs, mk_files, master_files


def list_files(directory):
    # Get files and folders in directory 
    abs_dir = os.listdir(directory)
    direct = directory + abs_dir[0] + '/'
    file_names = []

    # Iterate through files and sub-directories to find other files and create list of absolute file paths
    i = 0

    while i < len(abs_dir):
        # Create absolute path for file
        abs_file = os.path.join(directory, abs_dir[i])
        # If directory, parse it to list_files() function and add the resulting list it to our file_names list
        if os.path.isdir(abs_file):
            file_names += list_files(abs_file)
        # If just a file, append it to our file_names list
        elif abs_file.endswith('.txt'):
            file_names.append(abs_file)
        i += 1
            
    return sorted(file_names)


def main(master: str, flags: str, timestamp: str):
    if len(flags) == 2: 
        if flags[1] == "i":
            output = installation(master, timestamp)
        elif flags[1] == "v":
            output = verification(master, timestamp)
    elif flags[1] == "i" or flags[2] == "i":
        output = installation(master, timestamp)
    elif flags[1] == "v" or flags[2] == "v":
        output = verification(master, timestamp)
    
    i = 0

    while i < len(output):
        print(output[i])
        i += 1

    if len(flags) == 3:
        if flags[1] == "l" or flags[2] == "l":
            # Generate current date and time from timestamp
            timesplit = timestamp.split()
            cur_date = (f"{timesplit[2]}-{timesplit[1]}-{timesplit[0]}")
            cur_time = timesplit[3].replace(':', '_')

            logging(output, cur_date, cur_time)
   

if __name__ == "__main__":
    # If insufficient command lines arguments provided (no master directory given)
    if len(sys.argv) < 2:
        print("Insufficient arguments.", file=sys.stderr)
        exit(1)
    # If master directory exists
    elif not os.path.isdir(sys.argv[1]):
        print("Invalid master directory.", file=sys.stderr)
        exit(1)
    # If "/" missing at end of master directory
    elif sys.argv[1][-1] != "/":
        print("Invalid master directory.", file=sys.stderr)
        exit(1)
    # If flag not in command line arguments assign it default value
    elif len(sys.argv) < 3:
        flags = "-il"
    # If flag doesn't start with "-"
    elif sys.argv[2][0] != "-":
        print("Invalid flag. Flag must start with '-'.", file=sys.stderr)
        exit(1)
    # If flag has only log command
    elif sys.argv[2] == "-l":
        print("Invalid flag. Log can only run with install or verify.", file=sys.stderr)
        exit(1)
    # If flag has both verify and install commands
    elif sys.argv[2] == "-vi" or sys.argv[2] == "-iv":
        print("Invalid flag. Choose verify or install process not both.", file=sys.stderr)
        exit(1)
    # If flag has the same command repeated twice
    elif len(sys.argv[2]) == 3 and sys.argv[2][1] == sys.argv[2][2]:
        print("Invalid flag. Each character must be unique.", file=sys.stderr)
        exit(1)
    # If flag argument is too long
    elif len(sys.argv[2]) > 3:
        print("Invalid flag. Too many characters.")
        exit(1)
    # If flag has neither log, verify or install commands (l, v or i)
    elif len(sys.argv[2]) == 2 and sys.argv[2][1] != "l" and sys.argv[2][1] != "v" and sys.argv[2][1] != "i":
        print("Invalid flag. Character must be a combination of 'v' or 'i' and 'l'.", file=sys.stderr)
        exit(1)
    elif len(sys.argv[2]) == 3 and ((sys.argv[2][1] != "l" and sys.argv[2][1] != "v" and sys.argv[2][1] != "i") or 
            (sys.argv[2][2] != "l" and sys.argv[2][2] != "v" and sys.argv[2][2] != "i")):
        print("Invalid flag. Character must be a combination of 'v' or 'i' and 'l'.", file=sys.stderr)
        exit(1)
    # Assign command line arguments to variables
    else:
        flags = sys.argv[2]

    master = sys.argv[1]
    
    # Get current date and time
    timestamp = datetime.fromtimestamp(time.time()).strftime("%d %b %Y %H:%M:%S")

    main(master, flags, timestamp)

