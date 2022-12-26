#%%
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [8, 6]
plt.rcParams["figure.dpi"] = 200

from scipy.io.wavfile import read
from scipy.fft import fft, fftfreq

# Test segment
sample_rate, audio_data = read("../audio/1.wav")

# Two channel to one channel
if (len(audio_data) > 1):
    audio_data = np.mean(audio_data, axis=1)

time_to_plot = np.arange(sample_rate, sample_rate*1.3, dtype=int)
plt.plot(time_to_plot, audio_data[time_to_plot])

N = len(audio_data)
fft_res = fft(audio_data)
y = np.abs(fft_res[:N//2])
x = fftfreq(N)[:N//2]
plt.plot(x, y)

def create_time_freq_map(sample_rate, audio_data) -> list:
# Read input wav file
    pass
