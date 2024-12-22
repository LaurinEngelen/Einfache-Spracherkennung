from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .npy Datei
data = np.load('testdatensatz/test_rechts2.npy')
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
f = np.zeros(512)
border = 256
while(border + 256 < len(data)):
    fourier2 = np.fft.fft(data[border - 256:border + 256] * gaussianwindow)
    f = np.add(f, fourier2)
    border += 256
f = np.abs(np.divide(f, (border / 256) - 1))

freq = np.zeros(512)
for x in range(len(freq)):
    freq[x] = (x / (512 * 0.00015)) #eigentlich auch 1/44100, ergebnis aber useless
plt.plot(freq, f)
plt.grid()
plt.xlim(0, 1000)
plt.show()

