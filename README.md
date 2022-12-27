# DSP-Final-Project

## Environment setting
Please install the following packages first.
```
pip install tqdm glob pickle scipy
```

## Usage

```
python3 main.py {RECORDING_FILE} [-build {AUDIO_FILES_DIR}]
```

`-build` is used only when you want to update database! For example, you modified some parameters.

`{AUDIO_FILES_DIR}` points to the directory you put your audios for building the database.
                    It is necessary when `-build` flag is given.

## parameters you can modified

* create_hashes.py:
    * `freq_bits`: How many bits to represent the frequency in hash value.
    * `fanout_size`: For each point pair, when building hash table, only the time difference less than `fanout_size` ((1/2`swnd_length`)*`fanout_size` seconds) will be considered. (See original paper)
* create_time_freq_map.py:
    * `swnd_length`: The length(measure in seconds) of the sampling window.
    * `peaks_num`: The maximum number of peaks to calculate in a window, which means the number of peaks may less than `peaks_num` in practice.
    * `spread_distance`: The minimal distance between two peak frequency, used to prevent the situation such as 48, 49, 50, 51, 52 (Hz).

Currently using (I think it is nice by experiment.):
```
freq_bits       = 12
fanout_size     = 10
swnd_length     = 2
peaks_num       = 15
spread_distance = 200
```

**Try to make the difference between the answer and the candidates larger!**
![image](https://user-images.githubusercontent.com/71302574/209648116-9e0dee44-08ec-4bb1-a7f0-7855e9e7ef30.png)
![image](https://user-images.githubusercontent.com/71302574/209648193-cad1bde3-d0c7-4984-be10-7a289d3cba0a.png)

