import pygame
from Pyplop.Components.Import import COMPONENTS 

class gameObject:
    pos = pygame.Vector2( 100, 100 )
    vel = pygame.Vector2( 0, 0 )
    radius = 20
    color = "white"

    components = []

    def __init__( self, com ):
        self.components = com
    
    def setPos( self, pos ):
        self.pos = pos

    def update( self ):
        self.vel += pygame.Vector2( 0, 0.3 )
        self.pos += self.vel

    def getComponent( self, t ):
        for c in self.components:     
            if isinstance(c, COMPONENTS[t] ):
                return c

    def render( self, screen ):
        self.getComponent("render").render( self, screen )
        