import matplotlib.pyplot as plt
import numpy as np

# Einlesen der .npy Datei
data = np.load('testdatensatz/links2.npy')
data2 = np.load('testdatensatz/rechts2.npy')
freq = np.zeros(22050)

#data plotten
plt.plot(data)
plt.grid()
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.savefig('img/testamp.png')
plt.show()

#data2 plotten
plt.plot(data2)
plt.grid()
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.savefig('img/rechtsamp.png')
plt.show()

#data fouriertransformieren
spektrum = np.fft.fft(data[:22050])
# Negative Werte invertieren
spektrum = np.abs(spektrum)
# Formel um die Anzahl der Schwingungen in die Freuquenz umzurechnen: f = n / (M * t)
for x in range(len(freq)):
    freq[x] = (x / 1)# 44100 * 1/44100 = 1

# Darstellung des Amplitudenspektrums
plt.plot(freq, spektrum)
plt.grid()
plt.xlabel('Frequenz')
plt.ylabel('Amplitude')
plt.xlim(0, 1000)
plt.savefig('img/testspektrum.png')
plt.show()