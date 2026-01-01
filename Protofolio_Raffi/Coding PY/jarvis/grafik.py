import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math



point = np.array([
    [-1,-1,-1],
    [-1,-1, 1],
    [-1, 1,-1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1]
    
    ])


def rotasi_x(point, angle):
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    
    R = np.array([
        [1, 0, 0],
        [0, cos_a, -sin_a],
        [0, sin_a,cos_a],
        ])
    
    return point @ R.T

def rotasi_y(point,angle):
    rad = math.radians(angle)
    cos_b = math.cos(rad)
    sin_b = math.sin(rad)
    
    R = np.array([
        [cos_b, 0 , sin_b],
        [0 , 1 , 0],
        [-sin_b , 0, cos_b]
        ])

    return point @ R.T

def rotasi_z(point,angle):
    rad = math.radians(angle)
    cos_c = math.cos(rad)
    sin_c = math.sin(rad)
    
    R = np.array([
        [cos_c, -sin_c, 0],
        [sin_c, cos_c , 0],
        [0 , 0, 1]
        ])
    
    return point @ R.T
    
    
def kubus(ax, point):
    gabung = [
        (0,1),(0,2),(0,3),(0,4),
        (1,3),(1,5),
        (2,3),(2,6),
        (3,7),
        (4,5),(4,6),
        (5,7),
        (6,7)
    ]
    
    
    for j,i in gabung:
        ax.plot(
            [point[j,0],point[i,0]],
            [point[j,1],point[i,1]],
            [point[j,2],point[i,2]], color = 'blue'
            )

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

rotade = rotasi_x(point,30)
rotade = rotasi_y(point,45)
rotade = rotasi_z(point,60)

kubus(ax,rotade)

ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
ax.set_zlim([-2,2])
ax.set_title('Coba')
plt.show()