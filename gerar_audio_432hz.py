import numpy as np
import wave
import struct
import subprocess
import os

sample_rate = 44100
duration = 180.0 # 3 minutos
num_samples = int(sample_rate * duration)
t = np.linspace(0, duration, num_samples, endpoint=False)

# Frequências sagradas
f_base = 432.0
f_octave = 216.0
f_drone = 108.0
binaural_theta = 6.0 # 6Hz Theta para sono profundo

# Canal Esquerdo (432Hz)
left = (
    0.35 * np.sin(2 * np.pi * f_base * t) +
    0.20 * np.sin(2 * np.pi * f_octave * t) +
    0.15 * np.sin(2 * np.pi * f_drone * t)
)

# Canal Direito (438Hz -> 6Hz diferença binaural)
right = (
    0.35 * np.sin(2 * np.pi * (f_base + binaural_theta) * t) +
    0.20 * np.sin(2 * np.pi * (f_octave + binaural_theta / 2) * t) +
    0.15 * np.sin(2 * np.pi * f_drone * t)
)

# Modulação de "Respiração Lunar" (Onda suave de 0.08 Hz = 1 respiração a cada 12 segundos)
breathing = 0.85 + 0.15 * np.sin(2 * np.pi * 0.08 * t)
left *= breathing
right *= breathing

# Ruído rosa sutil de fundo (emulando brisa cósmica/ondas)
noise = np.random.normal(0, 0.02, num_samples)
# Filtro simples passa-baixa para suavizar o ruído
noise = np.convolve(noise, np.ones(50)/50, mode='same')
left += noise * breathing
right += noise * breathing

# Fade in (4s) e Fade out (6s)
fade_in = np.linspace(0, 1, int(sample_rate * 4.0))
fade_out = np.linspace(1, 0, int(sample_rate * 6.0))
left[:len(fade_in)] *= fade_in
right[:len(fade_in)] *= fade_in
left[-len(fade_out):] *= fade_out
right[-len(fade_out):] *= fade_out

# Normalização de volume (-1.0 a +1.0)
peak = max(np.max(np.abs(left)), np.max(np.abs(right)))
if peak > 0:
    left = (left / peak) * 0.88
    right = (right / peak) * 0.88

# Interleave estéreo em 16-bit PCM
left_int = (left * 32767).astype(np.int16)
right_int = (right * 32767).astype(np.int16)
stereo = np.empty((num_samples * 2,), dtype=np.int16)
stereo[0::2] = left_int
stereo[1::2] = right_int

wav_path = 'temp_432hz.wav'
with wave.open(wav_path, 'wb') as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(stereo.tobytes())

print(f"WAV gerado: {wav_path} ({os.path.getsize(wav_path)/(1024*1024):.2f} MB)")

# Converter para MP3 de alta qualidade (192 kbps)
out_mp3_1 = 'assets/audio/frequencia-lunar-432hz.mp3'
out_mp3_2 = 'Frequencia_Lunar_432Hz_Mahila_Luz.mp3'

for out_mp3 in [out_mp3_1, out_mp3_2]:
    cmd = [
        'ffmpeg', '-y', '-i', wav_path,
        '-b:a', '192k',
        '-metadata', 'title=Frequência Quântica Lunar (432Hz)',
        '-metadata', 'artist=Mahila Luz',
        '-metadata', 'album=Harmonização Cósmica',
        out_mp3
    ]
    subprocess.run(cmd, check=True)
    print(f"MP3 gerado: {out_mp3} ({os.path.getsize(out_mp3)/(1024*1024):.2f} MB)")

if os.path.exists(wav_path):
    os.remove(wav_path)
print("Concluído com sucesso!")
