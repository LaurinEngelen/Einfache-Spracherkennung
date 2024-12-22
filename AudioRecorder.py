
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Parameter für die Aufnahme
FORMAT = pyaudio.paInt16  # 16-bit Auflösung
CHANNELS = 1              # Monokanal
RATE = 44100              # Abtastrate (Samples pro Sekunde)
CHUNK = 1024              # Anzahl der Frames pro Buffer
RECORD_SECONDS = 5        # Dauer der Aufnahme (in Sekunden)

# Eindeutiger Dateiname basierend auf Zeitstempel
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
npy_filename = f"rechts_{timestamp}.npy"

# PyAudio initialisieren
audio = pyaudio.PyAudio()

# Aufnahme starten
print("Aufnahme startet...")
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Aufnahme beendet.")

# Aufnahme stoppen und Ressourcen freigeben
stream.stop_stream()
stream.close()
audio.terminate()

# Konvertierung zu NumPy-Array
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# NumPy-Array speichern
np.save(npy_filename, audio_data)
print(f"NumPy-Datei gespeichert als {npy_filename}")

# Plot des Signals
time = np.linspace(0, len(audio_data) / RATE, num=len(audio_data))
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data)
plt.title("Audio-Signal")
plt.xlabel("Zeit [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()