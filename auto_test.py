import os
import glob
import subprocess

tests = glob.glob("./test_data/*.wav")

for i in tests:
    p = subprocess.Popen(f"python main.py \"{i}\"", shell=False)
    p.wait()

print("done")