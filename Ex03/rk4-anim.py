from rk4_threebody import three_body_sim
import numpy as np
import matplotlib.pyplot as plt
from userlib.mplmpanimator import MplAnimator

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    point1.set_data([],[])
    point2.set_data([],[])
    point3.set_data([],[])


def animate(i):
    s = 1
    tail = int(nsteps/10)

    line1.set_data(xlist[(i*s)-tail:i*s,0],xlist[(i*s)-tail:i*s,1])
    line2.set_data(xlist[(i*s)-tail:i*s,4],xlist[(i*s)-tail:i*s,5])
    line3.set_data(xlist[(i*s)-tail:i*s,8],xlist[(i*s)-tail:i*s,9])
    point1.set_data(xlist[i*s,0],xlist[i*s,1])
    point2.set_data(xlist[i*s,4],xlist[i*s,5])
    point3.set_data(xlist[i*s,8],xlist[i*s,9])
    plt.annotate(
        "frame = {}\ntime = {:.2f}s".format(i,tmax/nsteps*i),
        xy=(0, 1),
        xycoords='figure fraction',
        xytext=(0,-40),
        textcoords='offset pixels',
        fontsize=14,
        bbox=dict(ec='#ffffff',fc="1")
    )

if __name__ == "__main__":
    xinit = np.array([[
        -.97000436,
        .24308753,
        -.46620368,
        -.43236573,
        .97000436,
        -.24308753,
        -.46620368,
        -.43236573,
        .0,
        .0,
        .93240737,
        .86473146
    ]])
    nsteps = 1000
    tmax = 4
    xlist = three_body_sim(nsteps, tmax, xinit)

    # from here mostly animation stuff
    fig = plt.figure(figsize=(19.2, 10.8))
    ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

    # create artists before initial setup!
    line1, = ax.plot([], [], color='r', marker='.', markersize=0, linewidth=1, linestyle='-')
    point1, = ax.plot([], [], color='r', marker='.', markersize=6)
    line2, = ax.plot([], [], color='g', marker='.', markersize=0, linewidth=1, linestyle='-')
    point2, = ax.plot([], [], color='g', marker='.', markersize=6)
    line3, = ax.plot([], [], color='b', marker='.', markersize=0, linewidth=1, linestyle='-')
    point3, = ax.plot([], [], color='b', marker='.', markersize=6)

    animator = MplAnimator(fig, animate, nsteps+1, "rk4-anim", initialize = init)
    animator.start()