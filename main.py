'''
    Usage: python3 main.py {RECORDING_FILE} [-build {AUDIO_FILES_DIR}]
'''

import os
import sys
import subprocess

def main():
    # if os.path.exists("./modules") == False:
    os.chdir(os.path.dirname(__file__))
    
    if len(sys.argv) >= 4 and sys.argv[2] == "-build":
        p = subprocess.Popen("python3 ./modules/create_database.py " + sys.argv[3], shell=True)
        p.wait()

    elif len(sys.argv) >= 3 and sys.argv[1] == "-build":
        p = subprocess.Popen("python3 ./modules/create_database.py " + sys.argv[2], shell=True)
        p.wait()

    elif os.path.exists("./database/hashes_database.pickle") == False:
        print("You must have to build the database first!!")
        print("Usage: python3 main.py {RECORDING_FILE} [-build {AUDIO_FILES_DIR}]")
        exit(1)

    if len(sys.argv) < 2 or os.path.isfile(sys.argv[1]) == False:
        print("You must have to give recording file as input!!")
        print("Usage: python3 main.py {RECORDING_FILE} [-build {AUDIO_FILES_DIR}]")
        exit(1)

    p = subprocess.Popen("python3 ./modules/scoring.py " + sys.argv[1], shell=True)
    p.wait()

if __name__ == "__main__":
    main()