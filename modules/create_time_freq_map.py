# %%
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [8, 6]
plt.rcParams["figure.dpi"] = 200

# from scipy.io.wavfile import read
# from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, stft

# Test segment
# sample_rate, audio_data = read("../audio/1.wav")

def create_time_freq_map(sample_rate:int, audio_data) -> list:
    swnd_length = 2    # seconds
    swnd_samples = int(swnd_length * sample_rate)
    # swnd_sample += swnd_sample % 2
    peaks_num = 15
    spread_distance = 200

    # Two channel to one channel
    if len(audio_data.shape) > 1:
        audio_data = np.mean(audio_data, axis=1)

    # Pad the data to divide evenly into the windows
    amount_to_pad = swnd_samples - (audio_data.size % swnd_samples)
    audio_data = np.pad(audio_data, (0, amount_to_pad))

    # Perform Short Time Fourier Transform
    f, t, Zxx = stft(audio_data, sample_rate, nperseg=swnd_samples,
                     nfft=swnd_samples, return_onesided=True)

    
    time_freq_map = []
    for time_idx, freq in enumerate(Zxx.T):
        # freq is by default complex
        # Convert to real number for building spectrum
        spectrum = abs(freq)

        # Find peaks
        peaks, props = find_peaks(spectrum, prominence=0, distance=spread_distance)

        top = min(len(props["prominences"]), peaks_num)
        largest_peaks = np.argpartition(props["prominences"], -top)[-top:]
        for i in largest_peaks:
            peak = peaks[i]
            peak_frequency = f[peak]
            time_freq_map.append((time_idx, peak_frequency))
    
    return time_freq_map