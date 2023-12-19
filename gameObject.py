import pygame

class gameObject:
    pos = pygame.Vector2( 100, 100 )
    vel = pygame.Vector2( 0, 0 )
    radius = 20
    color = "white"
    
    def setPos( self, pos ):
        self.pos = pos

    def update( self ):
        self.vel += pygame.Vector2( 0, 0.3 )
        self.pos += self.vel

    def render( self ):
        pass
        