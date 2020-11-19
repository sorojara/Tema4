# Base para la solucion del Laboratorio 4

# Los parametros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

o = 4.20

# Variables aleatorias A y Z
vaX = stats.norm(0, np.sqrt(o))
vaY = stats.uniform(0, np.sqrt(o))

# Creacion del vector de tiempo
T = 100			# numero de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicializacion del proceso aleatorio X(t) con N realizaciones
N = 10
X_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creacion de las muestras del proceso x(t) (A y Z independientes)
for i in range(N):
	X = vaX.rvs()
	Y = vaY.rvs()
	w0 = np.pi
	x_t = X * np.cos(w0*t) + Y * np.sin(w0*t)
	X_t[i,:] = x_t

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicializacion de matriz de valores de correlacion para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelacion
plt.figure()

# Calculo de correlacion para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(X_t[n,:], np.roll(X_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teorico de correlacion
Rxx = o * np.cos(w0*taus)

# Graficas de correlacion para cada realizacion y la
plt.plot(taus, Rxx, '-.', lw=4, label='Correlacion teorica')
plt.title('Funciones de autocorrelacion de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{XX}(\tau)$')
plt.legend()
plt.show()
