import os
import glob

tests = glob.glob("./test_data/*.wav")

def job(audio_file):
    os.system("python3 main.py " + "\"" + audio_file + "\"")
    # print(audio_file)
        
threads = []
count = 0
for i in tests:
    count += 1
    if count == 10: break
    threads.append(threading.Thread(target=job, args=(i,)))
    threads[len(threads)-1].start()

#for i in range(len(tests)):
for i in range(count-1):
    threads[i].join()

print("done")