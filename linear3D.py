import numpy as np
import matplotlib.pyplot as plt

def rotateX(p, ang):
    m_rot = np.array([ 
        [1,0,0],
        [0, np.cos(np.deg2rad(ang)), -np.sin(np.deg2rad(ang))],
        [0, np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang))]
    ])

    rot = m_rot @ p

    return rot


def rotateY(p, ang):
    m_rot = np.array([ 
        [np.cos(np.deg2rad(ang)), 0, -np.sin(np.deg2rad(ang))],
        [0,1,0],
        [np.sin(np.deg2rad(ang)), 0, np.cos(np.deg2rad(ang))]
    ])

    rot = m_rot @ p

    return rot

def rotateZ(p, ang):
    m_rot = np.array([ 
        [np.cos(np.deg2rad(ang)), -np.sin(np.deg2rad(ang)),0],
        [np.sin(np.deg2rad(ang)), np.cos(np.deg2rad(ang)),0],
        [0,0,1]
    ])

    rot = m_rot @ p

    return rot

def girar_figura(figura, _angulo_rotacao):
    for i in range(len(figura)):
        vetor = rotateZ(figura[i], _angulo_rotacao)
        ax.plot(vetor[0], vetor[1], vetor[2], 'k-')
        figura[i] = vetor

def connectPoints(p_0, p_1):
    x1, x2 = p_0[0], p_1[0]
    y1, y2 = p_0[1], p_1[1]
    z1, z2 = p_0[2], p_1[2]

    #Linhas Coloridas Aleatoriamente
    ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')
    #Linhas Pretas
    #ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')

def createCubo():
    #CUBO CENTRALIZADO
    connectPoints(cubo[0], cubo[1])
    connectPoints(cubo[0], cubo[3])
    connectPoints(cubo[0], cubo[4])
    connectPoints(cubo[1], cubo[2])
    connectPoints(cubo[1], cubo[5])
    connectPoints(cubo[2], cubo[3])
    connectPoints(cubo[2], cubo[6])
    connectPoints(cubo[3], cubo[7])
    connectPoints(cubo[4], cubo[5])
    connectPoints(cubo[4], cubo[7])
    connectPoints(cubo[5], cubo[6])
    connectPoints(cubo[6], cubo[7])

    #CUBO DESCENTRALIZADO
    #connectPoints(cubo[0], cubo[1])
    #connectPoints(cubo[0], cubo[2])
    #connectPoints(cubo[0], cubo[4])
    #connectPoints(cubo[1], cubo[5])
    #connectPoints(cubo[1], cubo[3])
    #connectPoints(cubo[2], cubo[3])
    #connectPoints(cubo[2], cubo[6])
    #connectPoints(cubo[3], cubo[7])
    #connectPoints(cubo[4], cubo[5])
    #connectPoints(cubo[4], cubo[6])
    #connectPoints(cubo[5], cubo[7])
    #connectPoints(cubo[6], cubo[7])

def createTesseract():
    #TESSERACT
    #CUBO EXTERNO
    connectPoints(tesseract[0], tesseract[1])
    connectPoints(tesseract[0], tesseract[3])
    connectPoints(tesseract[0], tesseract[4])
    connectPoints(tesseract[1], tesseract[2])
    connectPoints(tesseract[1], tesseract[5])
    connectPoints(tesseract[2], tesseract[3])
    connectPoints(tesseract[2], tesseract[6])
    connectPoints(tesseract[3], tesseract[7])
    connectPoints(tesseract[4], tesseract[5])
    connectPoints(tesseract[4], tesseract[7])
    connectPoints(tesseract[5], tesseract[6])
    connectPoints(tesseract[6], tesseract[7])
    #CUBO INTERNO
    connectPoints(tesseract[0+8], tesseract[1+8])
    connectPoints(tesseract[0+8], tesseract[3+8])
    connectPoints(tesseract[0+8], tesseract[4+8])
    connectPoints(tesseract[1+8], tesseract[2+8])
    connectPoints(tesseract[1+8], tesseract[5+8])
    connectPoints(tesseract[2+8], tesseract[3+8])
    connectPoints(tesseract[2+8], tesseract[6+8])
    connectPoints(tesseract[3+8], tesseract[7+8])
    connectPoints(tesseract[4+8], tesseract[5+8])
    connectPoints(tesseract[4+8], tesseract[7+8])
    connectPoints(tesseract[5+8], tesseract[6+8])
    connectPoints(tesseract[6+8], tesseract[7+8])
    #CONEXÃO
    connectPoints(tesseract[0], tesseract[8])
    connectPoints(tesseract[1], tesseract[9])
    connectPoints(tesseract[2], tesseract[10])
    connectPoints(tesseract[3], tesseract[11])
    connectPoints(tesseract[4], tesseract[12])
    connectPoints(tesseract[5], tesseract[13])
    connectPoints(tesseract[6], tesseract[14])
    connectPoints(tesseract[7], tesseract[15])

#CUBO DESCENTRALIZADO
#cubo = [
#    [1, 1, 1], #0
#    [1, 6, 1], #1
#    [6, 1, 1], #2
#    [6, 6, 1], #3
#    [1, 1, 6], #4
#    [1, 6, 6], #5
#    [6, 1, 6], #6
#    [6, 6, 6]  #7
#]

#CUBO CENTRALIZADO
cubo = [
    [2, -2, -2], #0
    [-2, -2, -2], #1
    [-2, 2, -2], #2
    [2, 2, -2], #3
    [2, -2, 2], #4
    [-2, -2, 2], #5
    [-2, 2, 2], #6
    [2, 2, 2]  #7
]

#TESSERACT CENTRALIZADO
tesseract = [
    [2, -2, -2], #0
    [-2, -2, -2], #1
    [-2, 2, -2], #2
    [2, 2, -2], #3
    [2, -2, 2], #4
    [-2, -2, 2], #5
    [-2, 2, 2], #6
    [2, 2, 2],  #7
    [1, -1, -1], #8
    [-1, -1, -1], #9
    [-1, 1, -1], #10
    [1, 1, -1], #11
    [1, -1, 1], #12
    [-1, -1, 1], #13
    [-1, 1, 1], #14
    [1, 1, 1]  #15
]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])

createTesseract()
#createCubo()
#plt.show()

''' DEBUG
printed = False
print(len(ax.lines))
'''
while True:
    #girar_figura(cubo, 5)
    #createCubo()

    girar_figura(tesseract, 5)
    createTesseract()
    plt.draw()
    
    ''' DEBUG
    if (printed == False):
        print(len(ax.lines))
        printed = True
    '''
    
    #FOR CUBO
    #for i in range(len(ax.lines)-13, 0, -1):
    #    ax.lines.remove(ax.lines[i])

    #FOR TESSERACT
    for i in range(len(ax.lines)-33, 0, -1):
        ax.lines.remove(ax.lines[i])
    
    plt.pause(0.00001)

