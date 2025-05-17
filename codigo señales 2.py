import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt
from scipy.interpolate import interp1d

# === 1. CARGA Y PROCESAMIENTO DE LA IMAGEN ===
image_path = "ecgsara.png"
imagen = cv2.imread(image_path)
if imagen is None:
    raise FileNotFoundError(f"No se encontró la imagen: {image_path}")
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

rows = binary.shape[0]
ecg = []
for col in range(binary.shape[1]):
    column_data = binary[:, col]
    indices = np.where(column_data == 255)[0]
    value = rows - np.mean(indices) if len(indices) > 0 else rows / 2
    ecg.append(value)
ecg = np.array(ecg)
ecg = (ecg - np.min(ecg)) / (np.max(ecg) - np.min(ecg)) * 3.3  # Normalización

# === 2. INTERPOLACIÓN DE LA SEÑAL ===
fs = 250  # Hz
duracion = 15  # segundos
n = fs * duracion
t_original = np.linspace(0, 1, len(ecg))
t_nuevo = np.linspace(0, 1, n)
ecg_interp = interp1d(t_original, ecg, kind='linear')(t_nuevo)
t_ecg = np.linspace(0, duracion, len(ecg_interp))

# === 3. TRANSFORMADA WAVELET DISCRETA ===
wavelet = 'db4'
nivel_max = pywt.dwt_max_level(len(ecg_interp), pywt.Wavelet(wavelet).dec_len)
coeffs = pywt.wavedec(ecg_interp, wavelet, level=nivel_max)

# === 4. RECONSTRUCCIÓN DE DETALLES COMO MATRIZ UNIFORME ===
detalle_matrix = []
for i in range(1, len(coeffs)):
    coeffs_nivel = [np.zeros_like(c) for c in coeffs]
    coeffs_nivel[i] = coeffs[i]
    detalle_rec = pywt.waverec(coeffs_nivel, wavelet)
    detalle_rec = detalle_rec[:len(ecg_interp)]
    detalle_matrix.append(detalle_rec)
detalle_matrix = np.vstack(detalle_matrix)

# === 5. FRECUENCIAS APROXIMADAS EN HZ ===
frecuencias_y = [
    "62.5–125", "31.2–62.5", "15.6–31.2", "7.8–15.6",
    "3.9–7.8", "1.95–3.9", "0.98–1.95", "0.49–0.98"
][:nivel_max]
yticks_pos = np.arange(0.5, 0.5 + len(frecuencias_y), 1)

# === 6. GRAFICAR: SEÑAL + ESPECTROGRAMA ===
fig, axs = plt.subplots(2, 1, figsize=(14, 8), gridspec_kw={'height_ratios': [1, 2]})

# Señal ECG interpolada
axs[0].plot(t_ecg, ecg_interp, color='black')
axs[0].set_title('Señal ECG interpolada desde imagen')
axs[0].set_ylabel('Amplitud (V)')
axs[0].set_xlabel('Tiempo (s)')
axs[0].grid(True)

# === Aplicar límite a los coeficientes para mejor visualización ===
limite = np.percentile(np.abs(detalle_matrix), 98)

# Espectrograma wavelet con colores típicos
im = axs[1].imshow(
    np.abs(detalle_matrix),
    extent=[0, duracion, 0, nivel_max],
    aspect='auto',
    cmap='jet',
    origin='lower',
    vmin=0,
    vmax=limite
)
axs[1].set_title('Espectrograma Wavelet Discreta (Daubechies - db4)')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_ylabel('Frecuencia aproximada (Hz)')
axs[1].set_yticks(yticks_pos)
axs[1].set_yticklabels(frecuencias_y)
plt.colorbar(im, ax=axs[1], label='|Coeficiente|')
plt.tight_layout()

# Guardar imagen
plt.savefig("espectrograma_wavelet_jet.png", dpi=300)
plt.show()
