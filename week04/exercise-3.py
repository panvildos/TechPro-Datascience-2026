import numpy as np
from matplotlib import pyplot as plt
N = 4000
dur_f = 2
time = np.linspace(0,dur_f,N)

signal1_np = 0.1*np.sin(2*np.pi*time*20)
signal2_np = 2*np.sin(2*np.pi*time*1)

plt.plot(time,signal1_np)
plt.plot(time,signal2_np)

mic1 = .9*signal1_np + 0.1*signal2_np
mic2 = 0.5*signal1_np + 0.5*signal2_np
plt.plot(time,mic1)
plt.plot(time,mic2)


A = np.array([[0.9,0.5],[0.1,0.5]])

signal1_np = signal1_np.reshape(N,1)
signal2_np = signal2_np.reshape(N,1)
sources_arr = np.concatenate( (signal1_np, signal2_np) , axis=1)


mics_arr = sources_arr.dot(A)
mics_arr.shape

B = np.linalg.inv(A)
recon_arr = mics_arr.dot(B)

plt.plot(recon_arr)


