import pygame
from Pyplop.gameObject import gameObject 
from Pyplop.Components.Import import importComponents 
from Pyplop.Console.console import Console


class pyPlop:

    clock = pygame.time.Clock()
    running = True
    dt = 0
    gameObjects = []

    def __init__( self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.gameConsole = Console( self.screen )
        

    def run( self ):
        while self.running:
            self.running = checkQuit()

            self.screen.fill( (13, 16, 23) )
            
            for obj in self.gameObjects:
                obj.render( self.screen )
                obj.update()

            if self.gameConsole.active:
                self.gameConsole.render()

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

    def add( self, config ):
        newObj = gameObject( config )
        self.gameObjects.append( newObj )

        return newObj      
    
importComponents(pyPlop)

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                return False
    return True




