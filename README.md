# DSP-Final-Project

# **Note: Put your audio files into audio/**

## Usage

`python3 main.py {AUDIOFILE} [-build]`

`-build` is used only when you want to update database! For example, you modified some parameters.

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

**Try to make the difference between the answer and the candidates larger!**

![image](https://user-images.githubusercontent.com/71302574/209581424-e84a2e3f-2a7c-40c7-a231-b4093135447b.png)
![image](https://user-images.githubusercontent.com/71302574/209581442-94ae38d2-c46b-41cc-ae82-c685cc6426b0.png)
