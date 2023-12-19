import pygame
from gameObject import gameObject 
from RenderTypes import RenderT 
from console import Console

class pyPlop:

    clock = pygame.time.Clock()
    running = True
    dt = 0
    gameObjects = []

    def __init__( self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.gameConsole = Console( self.screen )
        setattr(self, 'render', RenderT )

    def run( self ):
        while self.running:
            self.running = checkQuit()

            self.screen.fill( (13, 16, 23) )
            
            for obj in self.gameObjects:
                obj.render( obj, self.screen )
                obj.update()

            if self.gameConsole.active:
                self.gameConsole.render()

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000

    def add( self, config ):
        newObj = gameObject()
        newObj.setPos( config["pos"] )
        setattr(newObj, 'render', config["render"] )

        self.gameObjects.append( newObj )

        return newObj, self      

    def pos( x, y ):
        return pygame.Vector2( x, y )
    
    

def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                return False
    return True




