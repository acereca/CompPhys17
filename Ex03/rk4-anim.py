from rk4_threebody import three_body_sim
import matplotlib.animation as anim
import matplotlib.patches as pat
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import subprocess

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
fig = plt.figure(figsize=(19.2,10.8))
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

#create artists before initial setup!
line1, = ax.plot([], [], color='r', marker='.', markersize=0, linewidth=1, linestyle='-')
point1, = ax.plot([], [], color='r', marker='.', markersize=6)
line2, = ax.plot([], [], color='g', marker='.', markersize=0, linewidth=1, linestyle='-')
point2, = ax.plot([], [], color='g', marker='.', markersize=6)
line3, = ax.plot([], [], color='b', marker='.', markersize=0, linewidth=1, linestyle='-')
point3, = ax.plot([], [], color='b', marker='.', markersize=6)

#vec1 = pat.Arrow(0,0,0,0)

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
    tail = int(nsteps/10)
    #print("frame: {}".format(i))
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
    return line1,line2,line3, point1,point2,point3

def create_file(startFrame: int, stopFrame: int, filePart: int, fps: int = 60):
    moviewriter = anim.FFMpegWriter(fps=fps,codec='libx264')
    fname = 'p_{:02}.mp4'.format(filePart)
    moviewriter.setup(fig, fname, dpi=100)
    for j in range(startFrame, stopFrame):
        animate(j)
        moviewriter.grab_frame()
    moviewriter.finish()

def multiP(nFrames: int, nProc: int = 4):
    p = []
    for i in range(nProc):
        p.append(multiprocessing.Process(target=create_file, args=(int(nFrames/nProc)*i, int(nFrames/nProc)*(i+1), i)))
        p[i].start()

    for pr in p:
        pr.join()



if __name__=="__main__":
    nParts = 4
    multiP(nsteps, nParts)
    fname = "rk4-anim"
    import os
    fdir = os.path.dirname(os.path.realpath(__file__))

    foundStr = ""
    for i in range(nParts):
        foundStr += "file " + fdir + "/p_{:02}.mp4".format(i) + "\n"

    with open("temp", 'w') as f:
        f.write(foundStr)

    concatCmd = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", "temp", "-c", "copy", "{}.mp4".format(fname)]

    p = subprocess.Popen(concatCmd)
    p.wait()


    cleanupCmd = ["find", fdir, "-name", "p_[0-9][0-9].mp4", "-delete"]
    subprocess.call(cleanupCmd)

    rmTemp = ['rm', fdir +'/temp']
    subprocess.call(rmTemp)
