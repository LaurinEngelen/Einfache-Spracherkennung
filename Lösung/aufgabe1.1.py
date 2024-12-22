import pyaudio
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
print("running")
for x in range(5):
    print("Sample", x)
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=SAMPLEFREQ,
                    input=True, frames_per_buffer=FRAMESIZE)
    data = stream.read(NOFFRAMES*FRAMESIZE)
    decoded = np.frombuffer(data, dtype=np.int16)
    start = 0
    i = 0
    while(i < len(decoded) and start == 0):
       if(decoded[i] >= 1000 or decoded[i] <= -1000):
           start = i
       i += 1
    decoded = decoded[i:i + 44100]      
    np.save("testx"+ str(x), decoded)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    plt.plot(decoded)
    plt.show()

print("done")
plt.plot(decoded)
loc, labels = plt.xticks()
loc = loc[1:len(loc) - 1]
newlabels = []
for x in loc:
    newlabels.append(round(x * (1000 / SAMPLEFREQ), 2))
plt.xticks(loc, newlabels)
plt.xlim(0)
plt.title("Testaufnahme")
plt.xlabel("Zeit [ms]")
plt.ylabel("Amplitude [DN]")
plt.show()