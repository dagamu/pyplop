from Pyplop.Components.RenderTypes import RenderT 
from Pyplop.Components.Pos import Pos 
import pygame

COMPONENTS = {
    "pos": Pos,
    "render": RenderT,
    "collider": Pos,
    "rigid": Pos,
}

def importComponents( pyPlop ):
    for key, c in COMPONENTS.items():
        setattr(pyPlop, key, c )