import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))


#function that integrates the 2 - body - problem using the leapfrog
#algorithm. The initial velocity needs to be two dimensional
#vector, the step size h can be choosen. The program breaks when the
#orbit is complete.
def leapfrog(v_0, h, s_0 = np.array([0, 1])):
    S = [s_0]   #list for spatial coordinate
    V = [v_0]   #list for relative velocity
    E = []      #list for the Energy
    #first value for the acceleration
    a = [-1*(np.array([(S[-1])[0], (S[-1])[1]]))/(((S[-1]**2)[0] + (S[-1]**2)[1])**1.5)]
    test = 0    #variable to check if the orbit is complete
    step = 0
    maxstep = 1000000

    while((test < 2) and (step < maxstep)):
        vhalf = V[-1] + 0.5*h*a[-1]
        S.append(S[-1] + h*vhalf)
        a.append(-1*(np.array([(S[-1])[0], (S[-1])[1]]))/(((S[-1]**2)[0] + (S[-1]**2)[1])**1.5))
        V.append(vhalf + 0.5*h*a[-1])
        E.append((0.5*((V[-1]**2)[0] + (V[-1]**2)[1])) - (1/((S[-1]**2)[0] + (S[-1]**2)[1])**0.5))

        if ((S[-1])[0] < 0):
            test = 1
        if (test == 1 and (S[-1])[0] > 0):
            test = 2

    return np.array(S), np.array(V), np.array(E)


#for the given initial values the eccentricity is zero,
#therefore the orbit is circular
orbits = [1, 0],[1.3,0],[.8,0]

for o in orbits:
    S, V, E = leapfrog(np.array(o), 0.0001)
    plt.plot(S[:, 0], S[:, 1], label="$v_{init}$=" + "{}".format(o[0]))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal')
plt.savefig('fig_b1.png')
plt.clf()
# plt.cla()
# plt.close()

for o in orbits:
    energyerror = []
    H = [0.01, 0.001, 0.0001, 0.0001, 0.00001]
    for h in H:
        S, V, E = leapfrog(np.array(o), h)
        energyerror.append((abs(E[-1] - E[0])) / (abs(E[0])))

    plt.plot(H, energyerror, label="$v_{init}$=" + "{}".format(o[0]))

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Stepsize h')
plt.ylabel('error in energy')
plt.legend()
plt.savefig('fig_b2.png')
