'''
    Hash function: 32-bit int for value: | frequency f1 | frequency f2 | time difference |
                                             12 bits        12 bits          10 bits
    hash(value) = (song_id, time)
    
    Use to create hashes for a given point,
    with a set of points ahead in time up to swnd_num sampling windows length.

    Return:
        Hash table for the song.
'''
def create_hashes(time_freq_map:list, song_id:int) -> dict:
    hashes = {}
    max_freq = 24_000    # Sampling rate: 48k Hz
    freq_bits = 12
    fanout_size = 10

    for idx, (time, freq) in enumerate(time_freq_map):
        # Iterate the next n pairs to produce hashes
        # n = peaks_num * (swnd_num+1)

        for other_time, other_freq in time_freq_map[idx:]:
            diff = other_time - time
            # If time difference too small or large, ignore
            if diff < 1:
                continue
            if diff > fanout_size:
                break
            
            # Place the freq into 10 bits
            freq_10bit = freq / max_freq * (2**freq_bits)
            other_freq_10bit = other_freq / max_freq * (2**freq_bits)

            # Produce a 32-bit hash
            hash = (int(freq_10bit) << 22) | (int(other_freq_10bit) << 10) | int(diff)
            hashes[hash] = (song_id, time)
    
    return hashes