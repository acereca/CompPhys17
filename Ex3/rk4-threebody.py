from rk4 import rKN
import numpy as np
import matplotlib.pyplot as plt

# calculating gravitational acceleration
def grav_acc(
    m1: float,
    x1: float,
    y1: float,
    m2: float,
    x2: float,
    y2: float) -> (float,float):

    G = 1 # m^3/kg/s^2

    r = np.array([x2-x1,y2-y1])
    a = G*m2/np.sqrt(r[1]**2+r[0]**2)**3*r
    return a

def three_body_sim(
        nsteps: int = 100,
        tmax: float = 1,
        init_val: np.ndarray(shape=(1,12))
    ) -> np.ndarray(shape=(nsteps+1,12)):

    # where (y_1+4i,y_2+4i) initial x,y coords of m_i and
    # (y_3+4i,y_4+4i) the initial x,y velocity of m_i
    # taken from exercise sheet no3

    xlist = np.ndarray(shape=(nsteps+1,12), dtype=float)
    xlist[0] = init_val


    # only dist dependent accelerations
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

    # runge-kutta using prev calculated values
    for i in range(nsteps):
        xlist[i+1] = rKN(xlist[i],fsys,tmax/nsteps)

    return xlist


if __name__=="__main__":

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

    xlist = three_body_sim(400,4,xinit)
