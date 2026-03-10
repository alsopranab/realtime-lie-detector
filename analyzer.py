import librosa
import numpy as np

def compute_stress(audio, sr):

    pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)

    pitch_vals = pitches[magnitudes > np.median(magnitudes)]

    if len(pitch_vals) == 0:
        return 0

    pitch_var = np.std(pitch_vals)

    energy = np.mean(librosa.feature.rms(y=audio))

    stress = (pitch_var * 0.6 + energy * 0.4) * 100

    return stress