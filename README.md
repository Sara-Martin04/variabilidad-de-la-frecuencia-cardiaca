# Variabilidad de la frecuencia cardiaca usando la Transformada de Wavelet

Para iniciar debemos conocer la siguiente información: 

## •	Actividad simpática y parasimpática del sistema nervioso autónomo
El sistema nervioso autónomo comienza en el cerebro, e incluye parte de la corteza cerebral de la ínsula, del cíngulo, de la amígdala y del tronco cerebral; éste último incluye la región periacueductal, el hipotálamo, el núcleo parabraquial de la protuberancia, el núcleo del tracto solitario y la región ventrolateral de la médula, la que es muy importante en el control de la presión arterial.

El sistema simpático regula algunas funciones más globales y difusas, en cambio, el parasimpático provee de controles más finos. Para satisfacer esas necesidades, el sistema simpático preganglionar sinapta lejos del órgano blanco, cerca de la médula espinal o cerebro, posee una sinapsis preganglionar corta y tiene largas conexiones postganglionares, mientras que el parasimpático lo hace cerca del órgano blanco, ejerciendo un control mucho más fino.

Sistema simpático: Se activa en situaciones de estrés, peligro o ejercicio. Prepara al cuerpo para actuar rápidamente.
Efectos principales:

	Aumenta la frecuencia cardíaca y la presión arterial.

	Dilata los broncodilatadores (más oxígeno).

	Inhibe la digestión.

	Dilata las pupilas (midriasis).

	Estimula la liberación de glucosa por el hígado.

	Contrae los vasos sanguíneos periféricos.

	Estimula las glándulas sudoríparas.

Sistema Parasimpático:  Se activa en momentos de reposo, relajación o digestión. Favorece el ahorro y la recuperación de energía.
Efectos principales:

	Disminuye la frecuencia cardíaca.

	Estimula la digestión y el peristaltismo.

	Contrae las pupilas (miosis).

	Estimula la secreción glandular (saliva, jugos gástricos).

	Promueve la micción y la defecación.  [1]

## •	Efecto de la actividad simpática y parasimpática en la frecuencia cardiaca


El sistema simpático aumenta la frecuencia cardíaca y la fuerza de las contracciones del músculo cardíaco y ensancha (dilata) las vías respiratorias para facilitar la respiración. Hace que el organismo libere la energía almacenada. La fuerza muscular aumenta. Este sistema también produce sudor en las palmas de las manos, dilatación de las pupilas y erección del vello. Hace más lentos los procesos corporales menos importantes en situaciones de emergencia, como la digestión y la micción. 
Por otra parte, el sistema parasimpático se dedica a conservar y restaurar. Retarda la frecuencia cardíaca y disminuye la presión arterial. Estimula el tubo digestivo para procesar los alimentos y eliminar los residuos. La energía procedente de la transformación de los alimentos se utiliza para restaurar y formar tejidos. [2]

## •	Variabilidad de la frecuencia cardiaca (HRV) medida como fluctuaciones en el intervalo R-R, y las frecuencias de interés en este análisis

La variabilidad de la frecuencia cardíaca se conoce como la variación en el tiempo que transcurre entre los intervalos RR del electrocardiograma y refleja la actividad del sistema nervioso autónomo sobre la función cardíaca. Su aumento se considera un factor protector para el corazón y su medición podría ser una herramienta predictiva temprana o diagnóstica en enfermedades cardiovasculares. El sistema nervioso autónomo genera efectos inotrópicos y cronotrópicos en la función cardíaca, que pueden aumentar o disminuir esta variabilidad.

El aumento o la disminución de la variabilidad de la frecuencia cardíaca están relacionados con la respuesta del sistema simpático y parasimpático; en otras palabras, la variación de tiempo en milisegundos que se da entre latido y latido está producida por la interacción del sistema nervioso autónomo con el sistema cardiovascular
La frecuencia cardíaca y variabilidad de la frecuencia cardíaca son inversamente proporcionales, además en el análisis de esta variación pueden influir distintos factores como edad, género, temperatura, hora del día, estado de actividad (activo o en reposo), carga de trabajo, consumo de alcohol o tabaco, entre muchos otros.

Para medir la variabilidad de la frecuencia cardiaca se utilizan distintos métodos, entre ellos el más común es el electrocardiograma, esta técnica muestra gráficamente cada una de las ondas R que se generan con cada latido, permitiendo el análisis del tiempo en milisegundos que hay entre los intervalos RR y las pequeñas variaciones que se pueden detectar entre intervalos consecutivos.

Otra forma de medir la variabilidad de la frecuencia cardíaca es mediante los aparatos portátiles POLAR, generalmente usados por deportistas, ya que permiten cuantificar los intervalos RR mientras la persona practica ejercicio físico
Con la ayuda de algunas técnicas como exponer a un paciente a estrés físico o administración de inotrópicos, se pueden hacer mediciones de laboratorio cortas de 2-5 minutos que permiten comparar la variabilidad de la frecuencia cardíaca de una persona antes y después de exponerlo a los estimuladores del sistema nervioso autónomo. [3]

## •	Transformada Wavelet: definición, usos y tipos de wavelet utilizadas en señales biológicas.  
La transformada wavelet es una técnica matemática que se usa para analizar señales que cambian con el tiempo, como las señales del corazón (ECG), del cerebro (EEG) o de los músculos (EMG). A diferencia de otras transformadas, como la de Fourier, la wavelet no solo muestra qué frecuencias hay en una señal, sino también en qué momento ocurren. Es como tener una lupa que te deja ver los detalles de la señal en diferentes escalas de tiempo, lo cual es muy útil porque las señales biológicas no son constantes y suelen tener muchos cambios rápidos.
Las wavelets se usan para cosas como:
•	Quitar el ruido que no nos sirve.
•	Detectar cosas importantes, como un latido raro.
•	Reducir el tamaño del archivo sin perder información importante.
•	Sacar datos útiles que después podemos usar para diagnosticar o alimentar un algoritmo.
Existen diferentes tipos de wavelets, y se eligen dependiendo del tipo de señal que se está analizando, como:

•	Daubechies (db): súper usadas, detectan bien los cambios rápidos.
![image](https://github.com/user-attachments/assets/15448129-6df3-4f79-80a7-230d143eb053)

•	Symlets (sym): parecidas a Daubechies, pero un poco más suaves.
 ![image](https://github.com/user-attachments/assets/dffa3e39-8e4f-4ea3-bdac-e3c6f57e8c50)
 
•	Coiflets (coif): buenas para ver detalles finos.
![image](https://github.com/user-attachments/assets/1e362a7b-d654-4331-93af-8cf23015d170)

•	Biorthogonales (bior): sirven mucho para limpiar señales.
![image](https://github.com/user-attachments/assets/27bfb228-a893-4607-bfa1-3831f9ee8f35)

•	Morlet y Mexican Hat: se usan cuando quieres ver cómo cambian las frecuencias con el tiempo (muy usadas en EEG).
![image](https://github.com/user-attachments/assets/9a5c34e8-926c-43c2-ab2a-467c448690ef)
![image](https://github.com/user-attachments/assets/8c5988bd-cc11-4ff1-aa62-da4f618745be)


## •	Desarrollo y resultados.
Antes de iniciar la practica diseñamos los pasos a seguir para un buen desallo de esta, con el siguiente diagrama:

![Imagen de WhatsApp 2025-05-14 a las 15 04 54_994e5665](https://github.com/user-attachments/assets/2eef5297-09b8-4deb-9cad-272934e1905e)

*Diagrama de flujo*

Iniciamos obteniendo la señal electrocardiofráfica (ECG) durante un periodo de tiempo de seis minutos, en ese lapso de tiempo adquirio la señal en estado de reposo (feliz - normal) y en estado de alteración (enojada), se obtuvo la siguiente señal:

![ecgsara](https://github.com/user-attachments/assets/af2a1bad-3a22-4e73-9984-74580d71198e)
*Señal ECG*

Una vez obtenida la señal, se procedio con su procesamiento, se aplico un flitro IIR-pasa banda, para la eliminacion de componentes no deseados y reduccion de ruido, ademas para identificar los picos R y asi poder evaluar su comportamiento, obtuvimos lo siguiente:

![filtro](https://github.com/user-attachments/assets/8cc9296b-51ea-4dc5-b865-9021edaf75a7)

*Señal filtrada*

Con el siguiente codigo:
````
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
````
Posteriormente, se identificaron los picos R presentes en la señal ECG y se calcularon los intervalos R-R, construyendo con ello una nueva señal basada en estos intervalos, se obtuvo lo siguiente:

![R-R](https://github.com/user-attachments/assets/8a32a49a-5abb-481e-b216-3f5408b8ae7c)

*Señal R-R*

Utilizando el siguiente codigo:
````
# Detección de picos R 
t = np.linspace(0, duracion_objetivo, len(ecg))
threshold = np.mean(ecg_filtrada) + 0.5 * np.std(ecg_filtrada) 
picos, _ = find_peaks(ecg_filtrada, height=threshold, distance=fs * 0.4)  

# Calcular los intervalos R-R
rr_intervals = np.diff(picos) / fs  
t_rr = t[picos[1:]]  
````
A partir de esta información, se realizó el análisis en el dominio del tiempo, extrayendo parámetros estadísticos relevantes como la media y desviación estándar de los intervalos R-R, lo que aparece incorporado en la grafica. 

Finalmente, se aplicó la transformada wavelet daubechies discreta, con el fin de obtener un espectrograma de la HRV que permitiera observar la evolución temporal de las componentes de baja y alta frecuencia, asociadas a la actividad simpática y parasimpática del sistema nervioso autónomo, obtuvimos lo siguiente:

![Imagen de WhatsApp 2025-05-11 a las 20 19 01_1731d284](https://github.com/user-attachments/assets/d1eec6ed-f028-4ad5-a64b-df9c3fdaab44)

*wavelet*

A partir del siguiente codigo:
````
wavelet = 'db4'
nivel_max = pywt.dwt_max_level(len(ecg_interp), pywt.Wavelet(wavelet).dec_len)
coeffs = pywt.wavedec(ecg_interp, wavelet, level=nivel_max)
````

Al observar el espectrograma wavelet de la señal ECG, que representa periodos de relajación y alterada, se puede ver que en la banda de baja frecuencia (0.5–15 Hz), donde se encuentran las ondas principales del ECG (P, QRS y T), hay una mayor concentración de energía entre los segundos 0 y 3, y nuevamente entre los 12 y 14 segundos, lo que podría reflejar los episodios de taquicardia con una actividad cardíaca más intensa. En cambio, durante los momentos intermedios (aproximadamente entre 4 y 10 segundos), la energía se distribuye de forma más estable, lo que coincide con un estado de relajación. En la banda de alta frecuencia (15–125 Hz), relacionada más con ruido o actividad muscular, se ven zonas rojas entre los segundos 0–2 y 6–10, lo que indica momentos de alta energía posiblemente vinculados a movimientos o interferencias. También hay actividad notable en las frecuencias más bajas (0.49–3.9 Hz), que puede deberse a componentes lentos del ECG, como la onda T, o a la variabilidad del ritmo cardíaco en relajación. En general, se observa un cambio en la potencia espectral a lo largo del tiempo, con una señal más intensa durante la taquicardia y más estable durante la relajación.

## Recomendaciones
-Python 3.9, pyedflib, matplotlib, QtWidgets, pywt

## Información de contacto
-est.paula.vcardenas@unimilitar.edu.co, est.sara.martin@unimilitar.edu.co, est.cristian.cmolina@unimilitar.edu.co

### Bibliografía:

[1] Fisiología del sistema nervioso autónomo. (s/f). Medwave.cl. Recuperado el 3 de mayo de 2025, de https://www.medwave.cl/puestadia/cursos/3347.html

[2] Coon, E. (2023, julio 3). Introducción al sistema nervioso autónomo. Manual MSD versión para público general; Manuales MSD. https://www.msdmanuals.com/es/hogar/enfermedades-cerebrales-medulares-y-nerviosas/trastornos-del-sistema-nervioso-aut%C3%B3nomo/introducci%C3%B3n-al-sistema-nervioso-aut%C3%B3nomo

[3] Veloza, L., Jiménez, C., Quiñones, D., Polanía, F., Pachón-Valero, L. C., & Rodríguez-Triviño, C. Y. (2019). Variabilidad de la frecuencia cardiaca como factor predictor de las enfermedades cardiovasculares. Revista colombiana de cardiologia, 26(4), 205–210. https://doi.org/10.1016/j.rccar.2019.01.006

[4] Introduction to Wavelet Families - MATLAB & Simulink. (s. f.). https://la.mathworks.com/help/wavelet/gs/introduction-to-the-wavelet-families.html
