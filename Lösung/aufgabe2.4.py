import numpy as np
from scipy.stats import pearsonr
import my

sPerC = 5   #samples per command
richtig = 0
richtigw = 0
quote = np.zeros(sPerC)
spektren = []
spektrenw = []
befehle = ["hoch", "tief", "rechts", "links"]
#Referenzspektren Laden
for command in befehle:
    spektren.append(np.load('referenz/' + command + '.npy'))
    spektrenw.append(np.load('referenz/window_' + command + '.npy'))
#Für jeden Testdatensatz alle 5 samples laden
for command in befehle:
    for x in range(sPerC):
        data = np.load('tobias/' + command + str(x) + '.npy')
        #data = np.load('testdatensatz/' + command + str(x) + '.npy')
        #data = np.load('training/' + command + str(x) + '.npy')
        fourier = np.abs(np.fft.fft(data))
        fourierw = my.windowFFT(data)
        #fft von sample mit allen 4 Referenzspektren vergleichen
        quote = []
        quotew = []
        
        for c in befehle:
            corr, _ = pearsonr(spektren[befehle.index(c)], fourier)
            quote.append(corr)
            #windowing
            corr, _ = pearsonr(spektrenw[befehle.index(c)], fourierw)
            quotew.append(corr)

        print(command + " " + str(x) + " erkannt als: " + befehle[np.argmax(quote)])
        if(command == befehle[np.argmax(quote)]): richtig += 1
        #windowing
        print(command + " " + str(x) + " erkannt als: " + befehle[np.argmax(quotew)] + "(windowing)")
        if(command == befehle[np.argmax(quotew)]): richtigw += 1
        

print(richtig, "von " + str(sPerC * len(befehle)) + " richtig erkannt("
      + str(richtig/(sPerC * len(befehle)) * 100) + "%)")
print("Mit Windowing:")
print(richtigw, "von " + str(sPerC * len(befehle)) + " richtig erkannt(" 
      + str(richtigw/(sPerC * len(befehle)) * 100) + "%)")

#covariance(X, Y) = (sum (x - mean(X)) * (y - mean(Y)) ) * 1/(n-1)
#Pearson = covariance(X, Y) / (stdv(X) * stdv(Y))
