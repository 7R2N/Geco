import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#TODO: add some things about handling events, understand whats going on with generating map
class Map:
    def __init__(self, tree):
        self.tree = tree
        self.zoom = 1.0
        self.xrot = 0.0
        self.yrot = 0.0
        self.xtrans = 0.0
        self.ytrans = 0.0

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
        for point in self.tree.map:
            glColor3f(1.0, 1.0, 1.0)
            glVertex3f(point.x, point.y, point.z)
        glEnd()

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.zoom += 0.1
                elif event.button == 5:
                    self.zoom -= 0.1
                elif event.button == 1:
                    pass
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    dx, dy = event.rel
                    self.yrot += dx
                    self.xrot += dy
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.xtrans += 0.1
                elif event.key == pygame.K_RIGHT:
                    self.xtrans -= 0.1
                elif event.key == pygame.K_UP:
                    self.ytrans -= 0.1
                elif event.key == pygame.K_DOWN:
                    self.ytrans += 0.1

    def run(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)

        clock = pygame.time.Clock()

        while True:
            self.handle_events()
            self.draw_map()
            clock.tick(60)
