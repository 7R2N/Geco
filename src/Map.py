import pygame
import random
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

    def draw_map(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(self.xtrans, self.ytrans, -5.0 * self.zoom)
        glRotatef(self.xrot, 1.0, 0.0, 0.0)
        glRotatef(self.yrot, 0.0, 1.0, 0.0)

        glBegin(GL_LINES)
        for point in self.tree.map:
            for i, connection in enumerate(point.connections):
                glColor3f(1.0, 1.0, 1.0)
                glVertex3f(point.x, point.y, point.z)
                glVertex3f(self.tree.map[connection].x, self.tree.map[connection].y, self.tree.map[connection].z)
        glEnd()

        glPointSize(10)
        glBegin(GL_POINTS)
        for agent in self.agents:
            glColor3f(1.0, 0.0, 0.0)
            position = self.tree.map[agent.position]
            destination = self.tree.map[agent.destination]
            ver_x = ((destination.x - position.x) / agent.destination_weight) * 0.1
            ver_y = ((destination.y - position.y) / agent.destination_weight) * 0.1
            ver_z = ((destination.z - position.z) / agent.destination_weight) * 0.1
            if position.x == destination.x and position.y == destination.y and position.z == destination.z:
                agent.moving = False
                glVertex3f(position.x + 0.1, position.y, position.z)
                glVertex3f(position.x + 0.1, position.y, position.z)
            else:
                agent.moving = True
                print(ver_x)
                glVertex3f(position.x + 0.1, position.y, position.z)
                position.x += ver_x
                position.y += ver_y
                position.z += ver_z
        glEnd()

        glPointSize(20)
        glBegin(GL_POINTS)
        for point in self.tree.map:
            glColor3f(1.0, 1.0, 1.0)
            glVertex3f(point.x, point.y, point.z)
        glEnd()

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
        while True:
            Logic.handle_events(self)

            self.draw_map()
            clock.tick(60)
