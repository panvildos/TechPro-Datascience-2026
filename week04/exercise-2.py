import numpy as np

w = [4,-1,8]
w = np.array(w) 
print(w)

# #1
norm=0
for i in w:
   norm = norm + i**2
print(norm**(1/2))

norm=np.linalg.norm(w)
print(norm)

w2 = w ** 2
norm = w2.sum() ** (1/2)
print(norm)

# #2

w = w / norm
print(w)

# #3

v = [5,2,-6]
v = np.array(v)

norm_v = np.linalg.norm(v)
norm_w = np.linalg.norm(w)

# #4
cosine = w.dot(v) / (norm_v * norm_w)
angle = np.arccos(cosine)
print(angle)










