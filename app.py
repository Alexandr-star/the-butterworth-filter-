from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


sample_rate, sample = wavfile.read('./Sound_v2.wav')
print('ok')
print(sample_rate)
print(sample.shape[0])

sample_time = sample.shape[0] / sample_rate
print(sample_time)

# Входные данные

# Порядок фильтра
order = 10 
# Критическая чачтота или частоты 
Wn = 0.05
# тип фильтра
type = 'lowpass' 
# Аналоговый фильтр
analog = True 
#Тип вывода: числитель / знаменатель («ba»), 
#ноль полюсов («zpk») или секции второго порядка («sos»). 
#Значение по умолчанию - «ba» для обратной совместимости,
#но «sos» следует использовать для фильтрации общего назначения.
output = {'ba', 'zpk', 'sos'}
# Частота дискретизации цифровой системы.
#fs 

times = np.linspace(0., sample_time, sample.shape[0])


sos = signal.butter(order, Wn, btype=type, fs=1000, output='sos')
filtered_sample = signal.sosfilt(sos, sample)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)


#ax1.plot(times, sample[:, 0], label="Left channel")
ax1.plot(times, sample[:, 1], label="Right channel")
ax1.legend()

#ax2.plot(times, filtered_sample[:, 0], label="Left channel")
ax2.plot(times, filtered_sample[:, 1], label="Right channel")
ax2.legend()
plt.tight_layout()

plt.show()

































