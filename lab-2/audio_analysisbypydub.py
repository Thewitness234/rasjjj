from pydub import AudioSegment
from pydub.playback import play

# Load an audio file
audio = AudioSegment.from_file("C:/Users/ACER/Desktop/Labwork/audiofiles/drum.wav")

# Play the loaded audio


# Speed up the audio
faster_audio = audio.speedup(playback_speed=1.5)
faster_audio.export("audiofiles/faster_sample.wav", format="wav")

play(faster_audio)


# Increase volume by 5 dB
louder_audio = audio + 15
louder_audio.export("audiofiles/louder_sample.wav", format="wav")
# play(audio)
play(louder_audio)



# Extract a 10-second segment
segment = audio[:5000]  # First 5 seconds
segment.export("audiofiles/segment.wav", format="wav")
play(segment)



import numpy as np
import soundfile as sf

# Parameters
duration = 5.0  # seconds
frequency = 440  # Hz (A4 note)
sampling_rate = 44100  # samples per second

# Generate time points
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate sine wave
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Save to WAV file
sf.write("audiofiles/sine_wave.wav", sine_wave, sampling_rate)



import matplotlib.pyplot as plt

# Plot the sine wave
plt.plot(t[:1000], sine_wave[:1000])  # Plot first 1000 samples
plt.title("Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
