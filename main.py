'''
    Usage: python3 main.py [audio file] [-build]
'''

import os
import sys
import subprocess

def main():
    if os.path.exists("./modules") == False:
        os.chdir(os.path.dirname(__file__))
    
    if os.path.exists("./database/hashes_database.pickle") == False:
        p = subprocess.Popen("python3 ./create_database.py", shell=True, cwd="./modules")
        p.wait()

    elif len(sys.argv) == 3 and sys.argv[2] == "-build":
        p = subprocess.Popen("python3 ./create_database.py", shell=True, cwd="./modules")
        p.wait()

    if len(sys.argv) < 2:
        print("You must have to give a recording file as input!!")
        print("Usage: python3 main.py [audio file] [-build]")
        exit(1)

    p = subprocess.Popen("python3 ./modules/scoring.py " + sys.argv[1], shell=True)
    p.wait()

if __name__ == "__main__":
    main()