#importar librerias
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import pywt

#Leer datos
Datos0=sio.loadmat('baseline_1.mat')
Datos1=sio.loadmat('InnerRaceFault_vload_1.mat')
Datos2=sio.loadmat('OuterRaceFault_1.mat')
import scipy.io
mat = scipy.io.loadmat('baseline_1.mat')

c
datas = np.array(Normal)
#Inner=Datos1['Channel_1']
#Outer=Datos2['Channel_1']

import h5py
# f = h5py.File('baseline_1.mat','r')
# datas = f.get('data/variable1')
# datas = np.array(datas) # For converting to a NumPy array

#Datos
Fs=200000 #sampling rate
dt=1/Fs
Nd=68000

scales=np.arange(1, 50)

x1=Normal[1:Nd,0]
x2=Inner[1:Nd,0]
x3=Outer[1:Nd,0]
x4=Ball[1:Nd,0]
x5=Combined[1:Nd,0]
t = np.linspace(0, (Nd-1)*dt, Nd)  # Intervalo de tiempo en segundos

wavlist = pywt.wavelist(kind='continuous')

cwt1,frec1 = pywt.cwt(x1,scales,'gaus1')
cwt2,frec2 = pywt.cwt(x2,scales,'gaus1')
cwt3,frec3 = pywt.cwt(x3,scales,'gaus1')
cwt4,frec4 = pywt.cwt(x4,scales,'gaus1')
cwt5,frec5 = pywt.cwt(x4,scales,'gaus1')

plt.pcolormesh(t,scales,cwt1,cmap='binary')
plt.ylabel('Escala', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('Normal', fontsize=18)
plt.show()

plt.pcolormesh(t,scales,cwt2,cmap='binary')
plt.ylabel('Escala', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('IRF', fontsize=18)
plt.show()

plt.pcolormesh(t,scales,cwt3,cmap='binary')
plt.ylabel('Escala', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('ORF', fontsize=18)
plt.show()

plt.pcolormesh(t,scales,cwt4,cmap='binary')
plt.ylabel('Escala', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('Ball_fault', fontsize=18)
plt.show()

plt.pcolormesh(t,scales,cwt5,cmap='binary')
plt.ylabel('Escala', fontsize=14)
plt.xlabel('Tiempo [sec]', fontsize=14)
plt.title('Combined_fault', fontsize=18)
plt.show()

