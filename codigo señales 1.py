import cv2
import numpy as np
import matplotlib.pyplot as plt
import pywt  # Importamos PyWavelets
from scipy.signal import butter, find_peaks
from scipy.interpolate import interp1d

# Cargar imagen ECG
image_path = "ecgsara.png"
imagen = cv2.imread(image_path)

# Preprocesamiento de imagen
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

# Extraer la señal desde la imagen binaria
rows = binary.shape[0]
ecg = []
for col in range(binary.shape[1]):
    column_data = binary[:, col]
    indices = np.where(column_data == 255)[0]
    value = rows - np.mean(indices) if len(indices) > 0 else rows / 2
    ecg.append(value)
ecg = np.array(ecg)
ecg = (ecg - np.min(ecg)) / (np.max(ecg) - np.min(ecg)) * 3.3

# Interpolación para duración de 6 minutos
fs = 250  # Hz
duracion_objetivo = 360  # segundos
n_muestras_objetivo = fs * duracion_objetivo
t_original = np.linspace(0, 1, len(ecg))
interp = interp1d(t_original, ecg, kind='linear')
t_nuevo = np.linspace(0, 1, n_muestras_objetivo)
ecg = interp(t_nuevo)

# Filtro IIR banda 0.5-40Hz
def aplicar_filtro_iir_manual(x, b, a):
    y = [0.0] * len(x)
    for n in range(len(x)):
        for i in range(len(b)):
            if n - i >= 0:
                y[n] += b[i] * x[n - i]
        for j in range(1, len(a)):
            if n - j >= 0:
                y[n] -= a[j] * y[n - j]
        y[n] = y[n] / a[0]
    return np.array(y)

# Coeficientes del filtro
lowcut = 0.5
highcut = 40.0
order = 4
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
from scipy.signal import butter
b, a = butter(order, [low, high], btype='band')

# Aplicar filtro
ecg_filtrada = aplicar_filtro_iir_manual(ecg, b, a)

# Detección de picos R usando un umbral dinámico
t = np.linspace(0, duracion_objetivo, len(ecg))
threshold = np.mean(ecg_filtrada) + 0.5 * np.std(ecg_filtrada)  # Umbral dinámico
picos, _ = find_peaks(ecg_filtrada, height=threshold, distance=fs * 0.4)  # Ajuste de distancia

# Calcular los intervalos R-R
rr_intervals = np.diff(picos) / fs  # Intervalos R-R en segundos
t_rr = t[picos[1:]]  # Tiempo correspondiente a los intervalos R-R

# Cálculo de parámetros HRV (dominio del tiempo) para los intervalos R-R
mean_rr = np.mean(rr_intervals)
std_rr = np.std(rr_intervals)

# Transformada Wavelet Discreta Daubechies (DWT) usando PyWavelets
# Usamos la wavelet Daubechies con 4 momentos (db4)
wavelet = 'db4'  # Definir la wavelet Daubechies
coeffs = pywt.wavedec(rr_intervals, wavelet)

# Crear la figura con dos subgráficas (ECG y intervalos R-R)
plt.figure(figsize=(16, 12))

# Graficar la señal ECG filtrada
plt.subplot(2, 1, 1)
plt.plot(t, ecg_filtrada, label='ECG Filtrada', color='b')
plt.plot(t[picos], ecg_filtrada[picos], 'rx', label='Picos R')
plt.title('ECG Filtrada con Picos R')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()

# Graficar los intervalos R-R
plt.subplot(2, 1, 2)
plt.plot(t_rr, rr_intervals, marker='o', label='Intervalos R-R', color='g')
plt.axhline(mean_rr, color='r', linestyle='--', label='Media R-R')
plt.fill_between(t_rr, mean_rr - std_rr, mean_rr + std_rr, color='red', alpha=0.2, label='±1 Desviación estándar')
plt.title('Intervalos R-R y Parámetros HRV')
plt.xlabel('Tiempo (s)')
plt.ylabel('Intervalos R-R (s)')
plt.grid(True)
plt.legend()

# Mostrar los valores de la media y desviación estándar en la gráfica de intervalos R-R
plt.text(0.95, 0.9, f'Media R-R: {mean_rr:.3f} s', transform=plt.gca().transAxes, fontsize=12, color='red', ha='right')
plt.text(0.95, 0.85, f'Desviación R-R: {std_rr:.3f} s', transform=plt.gca().transAxes, fontsize=12, color='red', ha='right')

# Ajustar el diseño
plt.tight_layout()

# Mostrar la primera figura (ECG y intervalos R-R)
plt.show()

# Crear una nueva ventana para el espectrograma (Gráfico 3)
# Ahora combinamos los coeficientes de los niveles para graficarlos de forma adecuada
plt.figure(figsize=(10, 6))
for i, coeff in enumerate(coeffs):
    plt.plot(coeff, label=f'Nivel {i+1}')
    
plt.title('Coeficientes de la DWT con Daubechies (db4)')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

# Mostrar la figura del espectrograma
plt.show()
