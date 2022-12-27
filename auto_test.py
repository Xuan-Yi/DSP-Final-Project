import os
import glob
import subprocess

tests = glob.glob("./test_data/*.wav")

for i in tests:
    p = subprocess.Popen(f"python3 main.py \"{i}\"", shell=True)
    p.wait()

print("done")