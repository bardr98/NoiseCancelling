import numpy as np
from scipy.io import wavfile

# Load the audio data
rate, data = wavfile.read('audio_file.wav')

# Compute the FFT of the audio signal
fft_data = np.fft.fft(data)

# Compute the power spectrum of the audio signal
power_spectrum = np.abs(fft_data) ** 2

# Compute the frequency bins
freq_bins = np.fft.fftfreq(data.shape[0], 1/rate)

# Find the index of the frequency bin corresponding to the noise frequency
noise_freq = 1000  # Replace with the frequency of the noise
noise_idx = np.abs(freq_bins - noise_freq).argmin()

# Set the power spectrum of the noise frequency bin to zero
power_spectrum[noise_idx] = 0

# Reconstruct the audio signal
filtered_data = np.fft.ifft(np.sqrt(power_spectrum) * fft_data).real.astype(np.int16)

# Save the filtered audio data to a file
wavfile.write('filtered_audio_file.wav', rate, filtered_data)
