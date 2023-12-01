
import pyglet
from pyglet.gl import *
import pyrr

vertices = [0, 0, 0,
             1, 0, 0,
             1, 1, 0,
             0, 1, 0,
             0, 0, 1,
             1, 0, 1,
             1, 1, 1,
             0, 1, 1]

edges = [0, 1,
         1, 2,
         2, 3,
         3, 0,
         4, 5,
         5, 6,
         6, 7,
         7, 4,
         0, 4,
         1, 5,
         2, 6,
         3, 7]

vertex_buffer = pyglet.graphics.vertex_buffer(24, ('v3f', vertices), ('e2i', edges))

def update(dt):
    pass

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -5)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glRotatef(1, 3, 1, 1)
    glBegin(GL_LINES)
    for i in range(0, len(edges), 2):
        glVertex3fv(vertices[edges[i]*3:edges[i]*3+3])
        glVertex3fv(vertices[edges