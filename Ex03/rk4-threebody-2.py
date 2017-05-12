import numpy as np
import matplotlib.pyplot as plt
from rk4_threebody import three_body_sim

if __name__=="__main__":

    xinit = np.array([[
        7/3.0,
        -1.0,
        -.0,
        -.0,
        -5/3.0,
        2.0,
        -.0,
        -.0,
        -5/3.0,
        -1.0,
        .0,
        .0
    ]])
    tmax = 4 # s
    plt.figure(figsize=(10.8,7.2))
    plt.xlabel('stepsize')
    plt.ylabel('minimum distance')
    nsteps = np.linspace(.1,.000001,1000)
    dist1 = []
    dist2 = []
    for stepsize in nsteps:
        print(stepsize)
        xlist = three_body_sim(min(int(tmax/stepsize),1000),tmax,xinit, [3,4,5])
        #print(xlist)
        #plt.plot(xlist[:,0],xlist[:,1],label = '$m_1, \Delta t={:.3f}$'.format(stepsize))
        #plt.plot(xlist[:,4],xlist[:,5],label = '$m_2, \Delta t={:.3f}$'.format(stepsize))
        #plt.plot(xlist[:,8],xlist[:,9],label = '$m_3, \Delta t={:.3f}$'.format(stepsize))
        xmin1 = np.min(np.abs(xlist[:,0]-xlist[:,4]))
        ymin1 = np.min(np.abs(xlist[:,1]-xlist[:,5]))
        xmin2 = np.min(np.abs(xlist[:,0]-xlist[:,8]))
        ymin2 = np.min(np.abs(xlist[:,1]-xlist[:,9]))

        dist1.append(np.sqrt((xmin1)**2+(ymin1)**2))
        dist2.append(np.sqrt((xmin2)**2+(ymin2)**2))

    plt.plot(nsteps, dist1)
    plt.plot(nsteps, dist2)

    plt.legend()
    plt.savefig('3-21-plot2.png', bbox_inches='tight')
    plt.show()
