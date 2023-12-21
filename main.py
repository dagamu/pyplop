from Pyplop.pyplop import pyPlop

game = pyPlop( 500, 500 )
player = game.add([ 
    pyPlop.pos(0,0),
    pyPlop.render.circle(),
    pyPlop.collider(0,0),
    pyPlop.rigid(0,0)
])

game.run()