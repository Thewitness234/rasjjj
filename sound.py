from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import soundfile as sf

# === Part 1: Audio Manipulation with Pydub ===

# Load an audio file
audio = AudioSegment.from_file("/home/ven/Documents/drum.wav")

# Play the loaded audio
play(audio)

# Speed up the audio
faster_audio = audio.speedup(playback_speed=1.5)
faster_audio.export("audio-clips/faster_sample.wav", format="wav")

# Play the faster audio
play(faster_audio)

# Increase volume by 15 dB
louder_audio = audio + 10
louder_audio.export("audio-clips/louder_sample.wav", format="wav")

# Play the louder audio
play(louder_audio)

# Extract the first 5-second segment
segment = audio[:5000]  # Extract 5 seconds
segment.export("audio-clips/segment.wav", format="wav")

# Play the segment
play(segment)

# === Part 2: Sine Wave Generation ===

# Parameters for sine wave
duration = 5.0  # Duration in seconds
frequency = 440  # Frequency in Hz (A4 note)
sampling_rate = 44100  # Sampling rate in samples per second


t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)


sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)


sf.write("audio-clips/sine_wave.wav", sine_wave, sampling_rate)
