import rk4-threebody.three_body_sim as tbs
import matplotlib.animation as anim
import matplotlib.patches as pat

# from here mostly animation stuff
fig = plt.figure(figsize=(19.2,10.8))
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line1, = ax.plot([], [], color='r', marker='.', markersize=0, linewidth=1, linestyle='-')
point1, = ax.plot([], [], color='r', marker='.', markersize=6)
line2, = ax.plot([], [], color='g', marker='.', markersize=0, linewidth=1, linestyle='-')
point2, = ax.plot([], [], color='g', marker='.', markersize=6)
line3, = ax.plot([], [], color='b', marker='.', markersize=0, linewidth=1, linestyle='-')
point3, = ax.plot([], [], color='b', marker='.', markersize=6)

vec1 = pat.Arrow(0,0,0,0)

def init():
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    point1.set_data([],[])
    point2.set_data([],[])
    point3.set_data([],[])
    return line1,line2,line3,point1, point2,point3

def animate(i):
    s = 1
    tail = int(nsteps/30)
    print("frame: {}".format(i))
    line1.set_data(xlist[(i*s)-tail:i*s,0],xlist[(i*s)-tail:i*s,1])
    line2.set_data(xlist[(i*s)-tail:i*s,4],xlist[(i*s)-tail:i*s,5])
    line3.set_data(xlist[(i*s)-tail:i*s,8],xlist[(i*s)-tail:i*s,9])
    point1.set_data(xlist[i*s,0],xlist[i*s,1])
    point2.set_data(xlist[i*s,4],xlist[i*s,5])
    point3.set_data(xlist[i*s,8],xlist[i*s,9])
    return line1,line2,line3, point1,point2,point3

ani = anim.FuncAnimation(fig, animate, init_func=init,
                                   frames=int((nsteps+1)), interval=1, blit=True)

ani.save('3-21-{:.4f}'.format(ssize) + '.mp4', fps=60, extra_args=['-vcodec', 'libx264'])
