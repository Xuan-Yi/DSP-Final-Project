# DSP-Final-Project

# **Put your audio files into audio/**

## parameters you can modified

* create_hashes.py:
    * `freq_bits`: How many bits to represent the frequency in hash value.
* create_time_freq_map.py:
    * `swnd_length`: The length(measure in seconds) of the sampling window.
    * `peaks_num`: The maximum number of peaks to calculate in a window, which means the number of peaks may less than `peaks_num` in practice.
    * `spread_distance`: The minimal distance between two peak frequency, used to prevent the situation such as 48, 49, 50, 51, 52 (Hz).

Currently using (I think it is nice by experiment.):
    `freq_bits = 12`
    `swnd_length = 2`
    `peaks_num = 15`
    `spread_distance = 200`