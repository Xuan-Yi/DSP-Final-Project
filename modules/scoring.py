'''
    Usage: python3 scoring.py {RECORDING_FILE}
'''

import pickle
import os
import sys
from scipy.io.wavfile import read
from create_time_freq_map import create_time_freq_map as c_t_f_m
from create_hashes import create_hashes as c_h

# Load out the database
originalCWD = os.getcwd()
os.chdir(os.path.dirname(__file__))
with open("../database/hashes_database.pickle", "rb") as db:
    database = pickle.load(db)
with open("../database/song_name_dict.pickle", "rb") as songs:
    song_name_dict = pickle.load(songs)

# Load a short recording (test sample)
os.chdir(originalCWD)
sample_rate, audio_data = read(sys.argv[1])
# Create hash
time_freq_map = c_t_f_m(sample_rate, audio_data)
hashes = c_h(time_freq_map, None)


# For each hash in the song, check if there's a match in database
# There will be multi-matches, so for each match:
#    Append to a hashmap with the hash value and the time based on song id
#
# matches_per_song[song_id] = [ (), (), ... ]
matches_per_song = {}

for hash, (_, sample_time) in hashes.items():
    if hash in database:
        for song_id, source_time in database[hash]:
            # Initialize the content in dictionary
            if song_id not in matches_per_song:
                matches_per_song[song_id] = []
            matches_per_song[song_id].append((hash, sample_time, source_time))


# Below are used to score and find which song is it
# Use diagonal method, the time difference should be the same
# scores[song_id] = (offset, score)
scores = {}

for song_id in range(0, len(song_name_dict)):
    if song_id not in matches_per_song:
        continue
    song_name = song_name_dict[song_id]
    
    # print(f"Total matches for {song_name}: {len( matches_per_song[song_id] )}")

    song_scores_by_offset = {}
    for hash, sample_time, source_time in matches_per_song[song_id]:
        offset = source_time - sample_time
        if offset not in song_scores_by_offset:
            song_scores_by_offset[offset] = 0
        song_scores_by_offset[offset] += 1

    # Find where the largest offset happens
    max = (0, 0)  # (offset, score)
    for offset, score in song_scores_by_offset.items():
        if score > max[1]:
            max = (offset, score)
    scores[song_id] = max

# print top five scores out
with open("result.txt", "a", encoding="utf-8") as r:
    top_five = sorted(scores.items(), key=lambda x: x[1][1], reverse=True)[:5]
    i = 0
    for song_id, score in top_five:
        song = song_name_dict[song_id].rsplit(".", 1)[0]
        if i == 0:    first = song
        i += 1
        print(f"{song}: {score[1]} points at time {score[0]}")
        # r.write(f"{song}: {score[1]} points at time {score[0]}\n")

    ans = sys.argv[1]
    print(f"\nThe song is {first}\n")
    r.write(f"{ans}: The song is {first}\n\n")