import pygame

class RenderT:
    def circle( obj, screen ):
        pygame.draw.circle( screen, obj.color, obj.pos, obj.radius )