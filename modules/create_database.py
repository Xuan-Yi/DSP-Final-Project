'''
    Generate a hash database for all the songs.
    Later used to find the match.
    Usage: python3 create_database.py {AUDIO_FILE_DIR}
'''

import glob
import pickle
import os
import sys
from typing import List, Dict, Tuple
from tqdm import tqdm
from scipy.io.wavfile import read

from create_time_freq_map import create_time_freq_map as c_t_f_m
from create_hashes import create_hashes as c_h

cwd = os.getcwd()
os.chdir(sys.argv[1])
songs = glob.glob('*.wav')
song_name_dict = {}
database: Dict[int, List[Tuple[int, int]]] = {}

# Go through each song
for idx, filename in enumerate(tqdm(sorted(songs))):
    song_name_dict[idx] = filename
    sample_rate, audio_data = read(filename)

    time_freq_map = c_t_f_m(sample_rate, audio_data)
    hashes = c_h(time_freq_map, idx)

    # print(time_freq_map)
    # print(hashes)

    # For each hash, append it to the List for this hash
    for hash, id_time_pair in hashes.items():
        if hash not in database:
            database[hash] = []
        database[hash].append(id_time_pair)

# print(database)
os.chdir(cwd)
with open("./database/hashes_database.pickle", "wb") as db:
    pickle.dump(database, db, pickle.DEFAULT_PROTOCOL)
with open("./database/song_name_dict.pickle", "wb") as songs:
    pickle.dump(song_name_dict, songs, pickle.DEFAULT_PROTOCOL)