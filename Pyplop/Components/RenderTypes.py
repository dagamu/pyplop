import pygame



class RenderT:
    def getRenderType(name, c ):
         setattr(RenderT, name, c )

class circle(RenderT):
        def render( self, obj, screen ):
            pygame.draw.circle( screen, obj.color, obj.pos, obj.radius )

RenderT.getRenderType( "circle", circle)