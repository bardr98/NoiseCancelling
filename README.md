# NoiseCancelling
Basic implementation of noise cancelling in Python:

1. The program reads an audio file using the wavfile.read() function from the SciPy library.
2. The Fast Fourier Transform (FFT) of the audio signal is computed using the NumPy library.
3. The power spectrum of the audio signal is computed by taking the absolute value of the FFT and squaring it.
4. The frequency bins corresponding to the FFT are computed using the NumPy fftfreq() function.
5. The frequency bin corresponding to the noise frequency is found using the np.abs() and argmin() functions from NumPy.
6. The power spectrum of the noise frequency bin is set to zero.
7. The filtered audio signal is reconstructed using the inverse FFT (ifft()) of the square root of the power spectrum multiplied by the FFT of the original audio signal.
8. The filtered audio data is saved to a new file using the wavfile.write() function from SciPy.
