import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import my

spektren = []
befehle = ["hoch", "tief", "rechts", "links"]
freq = np.zeros(44100)
for x in range(len(freq)):
    freq[x] = (x / (44100 * (1/44100)))
freqw = np.zeros(512)
for x in range(len(freqw)):
    freqw[x] = (x / (512 * (1/44100)))
for command in befehle:
    tmp = np.zeros(44100)
    tmpw = np.zeros(512)
    for x in range(5):
        data = np.load('training/' + command + str(x) + '.npy')
        # plt.plot(freq, np.abs(np.fft.fft(data)))
        # plt.title(command + str(x))
        # plt.xlim(0, 1000)
        # plt.show()
        fourier = np.fft.fft(data)
        tmp = np.add(tmp, fourier)
        #windowing fft
        fourierw = my.windowFFT(data)
        tmpw = np.add(tmpw, fourierw)
    #normal fft
    tmp = np.abs(np.divide(tmp, 5))
    plt.plot(freq, tmp)
    plt.title(command)
    plt.xlim(0, 1000)
    plt.savefig('img/' + command + '.png')
    plt.show()
    np.save("referenz/" + command, tmp)
    spektren.append(tmp)
    #fft using windowing
    tmpw = np.abs(np.divide(tmpw, 5))
    plt.plot(freqw[:len(tmpw)], tmpw)
    plt.title(command)
    plt.xlim(0, 10000)
    plt.savefig('img/window_' + command + '.png')
    plt.show()
    np.save("referenz/window_" + command, tmpw)
    
#covariance(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)
#Pearson = covariance(X, Y) / (stdv(X) * stdv(Y))
corr, _ = pearsonr(spektren[0], spektren[2])
print(corr)
corr, _ = pearsonr(spektren[3], spektren[2])
print(corr)