import pygame
import random
import math
from src.Logic import Logic
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# TODO: add some things about handling events, improve agent movement
class Map:
    def __init__(self, tree):
        self.tree = tree
        self.zoom = 1.0
        self.xrot = 0.0
        self.yrot = 0.0
        self.xtrans = 0.0
        self.ytrans = 0.0
        self.agents = []

    def draw_map(self,t):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(self.xtrans, self.ytrans, -5.0 * self.zoom)
        glRotatef(self.xrot, 1.0, 0.0, 0.0)
        glRotatef(self.yrot, 0.0, 1.0, 0.0)


        for point in self.tree.map:
            glLineWidth(3.0)
            glBegin(GL_LINES)
            for i, connection in enumerate(point.connections):
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(point.x, point.y, point.z)
                glVertex3f(self.tree.map[connection].x, self.tree.map[connection].y, self.tree.map[connection].z)
            glEnd()


        for agent in self.agents:
            glColor3f(1.0, 0.0, 0.0)
            position = self.tree.map[agent.position]
            destination = self.tree.map[agent.destination]

            cube_size = 0.1
            radius = 0.5
            angle = t / 60

            rot_x = radius * math.cos(angle)
            rot_y = radius * math.sin(angle)
            rot_z = radius * math.cos(angle)

            glPushMatrix()
            glTranslatef(position.x + rot_x, position.y + rot_y, position.z + rot_z)
            glScalef(cube_size, cube_size, cube_size)

            glRotatef(2.0 * t / 5, 1.0, 0.0, 0.0)
            glRotatef(2.0 * t / 5, 0.0, 1.0, 0.0)
            glRotatef(2.0 * t / 5, 0.0, 0.0, 1.0)
            glBegin(GL_QUADS)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, -1.0)


            # ver_x = ((destination.x - position.x) / agent.destination_weight) * t/60
            # ver_y = ((destination.y - position.y) / agent.destination_weight) * t/60
            # ver_z = ((destination.z - position.z) / agent.destination_weight) * t/60
            # if position.x == destination.x and position.y == destination.y and position.z == destination.z:
            #     agent.moving = False
            #     glVertex3f(position.x + 0.1, position.y, position.z)
            # else:
            #     agent.moving = True
            #     print(ver_x)
            #     glVertex3f(position.x + 0.1, position.y, position.z)
            #     position.x += ver_x
            #     position.y += ver_y
            #     position.z += ver_z
            # glVertex3f(position.x + rot_x, position.y + rot_y, position.z + rot_z)

        glEnd()

        glColor3f(0, 1, 0)
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(2.0)
        glBegin(GL_LINES)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glEnd()

        glPopMatrix()


        for point in self.tree.map:
            cube_size = 0.2
            glColor3f(1.0, 1.0, 1.0)
            glPushMatrix()
            glTranslatef(point.x, point.y, point.z)
            glScalef(cube_size, cube_size, cube_size)

            glBegin(GL_QUADS)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glEnd()

            glColor3f(1.0, 0.0, 0.0)
            glEnable(GL_LINE_SMOOTH)
            glLineWidth(3.0)
            glBegin(GL_LINES)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(-1.0, -1.0, 1.0)
            glVertex3f(-1.0, -1.0, -1.0)
            glVertex3f(1.0, -1.0, 1.0)
            glVertex3f(1.0, -1.0, -1.0)
            glVertex3f(1.0, 1.0, 1.0)
            glVertex3f(1.0, 1.0, -1.0)
            glVertex3f(-1.0, 1.0, 1.0)
            glVertex3f(-1.0, 1.0, -1.0)
            glEnd()

            glPopMatrix()

        pygame.display.flip()

    def add_agent(self, agent):
        self.agents.append(agent)

    def run(self):
        pygame.init()
        display = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Geco")

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)

        clock = pygame.time.Clock()
        t=0
        while True:
            Logic.handle_events(self)

            self.draw_map(t)
            t+=1
            clock.tick(60)
