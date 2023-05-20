import pygame


class Logic:
    def handle_events(self):
        press = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.zoom -= 0.1
                elif event.button == 5:
                    self.zoom += 0.1
                elif event.button == 1:
                    pass
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    dx, dy = event.rel
                    self.yrot += dx
                    self.xrot += dy

        if press[pygame.K_UP]:
            self.ytrans -= 0.1
        if press[pygame.K_DOWN]:
            self.ytrans += 0.1
        if press[pygame.K_LEFT]:
            self.xtrans += 0.1
        if press[pygame.K_RIGHT]:
            self.xtrans -= 0.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for agent in self.agents:
            connections = self.tree.map[agent.position]
            new_position = agent.nextposition(connections)
            agent.updateposition(new_position)
