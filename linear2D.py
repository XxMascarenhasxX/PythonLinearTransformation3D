import numpy as np
import matplotlib.pyplot as plt

#ROTATION MATRIX FOR X AXIS
def rotateX(p, ang):
    m_rot = np.array([ 
        [np.cos(np.deg2rad(ang)), -np.sin(np.deg2rad(ang))],
        [np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang))]
    ])

    rot = m_rot @ p

    return rot

def escalate(p, size):
    
    rot = size * p

    return rot


def CreateArrow(_list_x_y):
    for i in range(len(_list_x_y) - 1):
        connectPoints(_list_x_y[i], _list_x_y[i + 1])
    connectPoints(_list_x_y[-1], _list_x_y[0])

def rotate_figure(figure, _angulo_rotacao):
    for i in range(len(figure)):
        vetor = rotateX(figure[i], _angulo_rotacao)
        ax.plot(vetor[0], vetor[1], 'k-')
        figure[i] = vetor

def increase_figure(figure, size):
    for i in range(len(figure)):
        vetor = escalate(figure[i], size)
        ax.plot(vetor[0], vetor[1], 'k-')
        figure[i] = vetor

#CONNECT TWO VECTORS AND PLOT THE LINE
def connectPoints(p_0, p_1):
    x1, x2 = p_0[0], p_1[0]
    y1, y2 = p_0[1], p_1[1]

    #Random Collored Lines
    #ax.plot([x1, x2], [y1, y2])
    #Black Lines
    ax.plot([x1, x2], [y1, y2], 'k-')


#CENTRALIZED CUBE
arrow = [
    [0, 0], #0
    [0, 0.5], #1
    [5, 0.5], #2
    [5, 0.75], #3
    [6, 0.25], #4
    [5, -0.25], #5
    [5, 0] #6
]

fig, ax = plt.subplots()
ax.set_xlim([-15,15])
ax.set_ylim([-15,15])

#createCube()
#plt.show()

CreateArrow(arrow)

for frames in range(0, 90):
    rotate_figure(arrow, 1)
    CreateArrow(arrow)
    plt.draw()

    for i in range(len(ax.lines)-8, 0, -1):
        ax.lines.remove(ax.lines[i])
    #increase_figure(arrow, 2)
    plt.pause(0.0001)

for newFrames in range(0, 90):
    increase_figure(arrow, 1.01)
    CreateArrow(arrow)
    plt.draw()
    
    for i in range(len(ax.lines)-8, 0, -1):
            ax.lines.remove(ax.lines[i])
    plt.pause(0.0001)

CreateArrow(arrow)
plt.show()