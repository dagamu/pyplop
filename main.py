from pyplop import pyPlop

game = pyPlop( 500, 500 )
player = game.add({ 
    "pos": pyPlop.pos( 100, 100 ),
    "render": game.render.circle,
    "collider": True,
    "rigid": True
})

game.run()