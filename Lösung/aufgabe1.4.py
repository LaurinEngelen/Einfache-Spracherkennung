from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import my

# Einlesen der .npy Datei
data = np.load('testdatensatz/rechts2.npy')
freq = np.zeros(44100)
for x in range(len(freq)):
    freq[x] = (x / (44100 * (1/44100)))
gaussianwindow = signal.windows.gaussian(512, std=40)
fourier = np.abs(np.fft.fft(data))
plt.plot(data)
plt.grid()
plt.show()
plt.plot(freq, fourier)
plt.grid()
plt.xlim(0, 1000)
plt.show()
f = my.windowFFT(data)
freq = np.zeros(512)
for x in range(len(freq)):
    freq[x] = (x / (512 * 1/44100)) #eigentlich auch 1/44100, ergebnis aber useless
plt.plot(freq, f)
plt.grid()
plt.xlim(0, 10000)
plt.show()
