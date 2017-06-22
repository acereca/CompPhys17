import numpy as np

m = (
        (-1,0,0,20,30,5),
        (0,-1,0,1,3,7),
        (0,0,-1,4,10,20),
        (20,30,25,0,0,0),
        (3,3,3,0,0,0),
        (7,8,20,0,0,0)
    )

m = np.array(m)
print(m)

w, v = np.linalg.eig(m)

print(w)
print(v)
