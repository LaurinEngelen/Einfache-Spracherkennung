from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .npy Datei
data = np.load('testdatensatz/test_rechts2.npy')
window = np.zeros((879, 512))
z = 256
freq = np.zeros(22050)
gaussianwindow = signal.windows.gaussian(512, std=4)
fourier = np.abs(np.fft.fft(data))
plt.plot(fourier)
plt.grid()
plt.xlim(0, 1000)
plt.show()
for y in range(0, 879):
    z = z - 512
    for x in range(0, 512):
        window[y, x] = np.mean(np.abs(np.fft.fft(data[z] * gaussianwindow)))
        z = z + 1

# Darstellung des Amplitudenspektrums
plt.plot(gaussianwindow)
plt.grid(True)
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.savefig('img/gauss.png')
plt.show()

# Darstellung des Amplitudenspektrums
plt.plot(window)
plt.grid(True)
plt.xlabel('Windows')
plt.ylabel('Amplitude')
plt.savefig('img/Alle.png')
plt.show()

for y in range(0, 879):
    for x in range(0, 512):
        window[y][x] = window[y][x] * gaussianwindow[x]
    window[y] = np.abs(np.fft.fft(window[y]))
    window[y] = np.mean(window[y])

plt.plot(window, 'r')
plt.grid(True)
plt.xlabel('Windows')
plt.ylabel('Amplitude')
plt.savefig('img/AlleRichtig.png')
plt.show()

# Der zweite Wert wird absolut minus den ersten absoluten wert gerechnet um später den Wert
difference = 2 / len(data)
# Die zweite Spalte der .csv Datei wird Fouriertransformiert
fourier = np.fft.fft(window)
# Die Fouriertransformierte Frequenz wird absolutiert, so dass kein negativer Wert mehr vorzufinden ist
spektrum = np.abs(fourier)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen - f = n / (M * t)
for x in range(len(freq)):
    freq[x] = (x / (difference * 22050))

plt.plot(freq, 'r')
plt.grid(True)
plt.xlabel('Windows')
plt.ylabel('Frequenz')
plt.savefig('img/ampwin.png')
plt.show()