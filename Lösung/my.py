from scipy import signal
import numpy as np

def windowFFT(data):
    gaussianwindow = signal.windows.gaussian(512, std=40)
    f = np.zeros(512)
    border = 256
    while(border + 256 < len(data)):
        #window ausschneiden, mit gaussfunktion multiplizieren und fft anwenden
        fourier2 = np.fft.fft(data[border - 256:border + 256] * gaussianwindow)
        #einzelne spektren aufaddieren
        f = np.add(f, fourier2)
        border += 256
    #aufaddierte spektren durch anzahl teilen (mittelwert)
    f = np.abs(np.divide(f, (border / 256) - 1))
    return f



