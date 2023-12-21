import pygame

class Pos:

    vec = pygame.Vector2( 0, 0)

    def __init__( self, x, y):
        self.vec = pygame.Vector2( x, y)

    def get( self ):
        return self.vec