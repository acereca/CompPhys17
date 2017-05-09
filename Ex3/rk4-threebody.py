from rk4 import rKN
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.patches as pat

nsteps = 10000
tmax = 1
tdata = np.linspace(0,tmax, nsteps+1)



# where (y_1+4i,y_2+4i) initial x,y coords of m_i and
# (y_3+4i,y_4+4i) the initial x,y velocity of m_i
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

xlist = np.ndarray(shape=(nsteps+1,xinit.shape[1]), dtype=float)
xlist[0] = xinit
def grav_acc(
    m1: float,
    x1: float,
    y1: float,
    m2: float,
    x2: float,
    y2: float):

    G = 1 # m^3/kg/s^2

    r = np.array([x2-x1,y2-y1])
    a = G*m2/r/np.sqrt(r[1]**2+r[0]**2)

    return a

a12 = lambda x: grav_acc(1,x[0],x[1],1,x[4],x[5])
a13 = lambda x: grav_acc(1,x[0],x[1],1,x[8],x[9])
a23 = lambda x: grav_acc(1,x[4],x[5],1,x[8],x[9])

# system of linear equations for three body system
fsys = [
    lambda x: x[2],             # dx_1
    lambda x: x[3],             # dy_1
    lambda x: a12(x)[0] + a13(x)[0],  # dv_x1
    lambda x: a12(x)[1] + a13(x)[1],  # dv_y1

    lambda x: x[6],             # dx_2
    lambda x: x[7],             # dy_2
    lambda x: -a12(x)[0] + a23(x)[0], # dv_x2
    lambda x: -a12(x)[1] + a23(x)[1], # dv_y2

    lambda x: x[10],            # dx_3
    lambda x: x[11],            # dy_3
    lambda x: -a23(x)[0] - a13(x)[0], # dv_x3
    lambda x: -a23(x)[1] - a13(x)[1]  # dv_y3
]


for i in range(nsteps):
    xlist[i+1] = rKN(xlist[i],fsys,tmax/(nsteps))

fig = plt.figure()
ax = plt.axes(xlim=(-3, 3), ylim=(-3, 3))
line1, = ax.plot([], [], color='r')
line2, = ax.plot([], [], color='g')
line3, = ax.plot([], [], color='b')

vec1 = pat.Arrow(0,0,0,0)

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    ax.add_patch(vec1)

    return line1,line2,line3,vec1

def animate(i, debug_patch):
    s = 50

    line1.set_data(xlist[:i*s,0],xlist[:i*s,1])
    line2.set_data(xlist[:i*s,4],xlist[:i*s,5])
    line3.set_data(xlist[:i*s,8],xlist[:i*s,9])
    debug_patch.remove()
    debug_patch = pat.Arrow(xlist[i*s,4],xlist[i*s,5],xlist[i*s,6]/2,xlist[i*s,7]/2, width=.05)
    ax.add_patch(debug_patch)
    return line1,line2,line3,vec1

ani = anim.FuncAnimation(fig, lambda i:animate(i, vec1), init_func=init,
                                   frames=int((nsteps+1)/50), interval=1, blit=True)

ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
