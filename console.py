import pygame
from pygame.locals import * 
from consoleFunc import consoleFunc

class Console:

    active = True
    focusInput = True

    topLeft = pygame.Vector2( 15, 20 )
    bottomLeft = pygame.Vector2( 15, -40 )

    consoleInput = "Placeholder"

    consoleHistory = []
    variables = []
    keyObjs = []

    inputCooldown = 0

    def __init__(self, screen ):
        self.font = pygame.font.Font('freesansbold.ttf', 12)
        self.surface = screen
        self.inputSize = ( screen.get_width() / 2, 15 )
        self.inputPos = ( 15, screen.get_height() - 30 )
        self.bottomLeft += (0, screen.get_height())

        self.variables.append(self.font.render(str( self.inputSize[0] ), True, (255, 255, 255) ))
        self.variables.append(self.font.render('Lorem', True, (255, 255, 255)))

        self.keyObjs = list( filter( filterKeysfromCons, vars(pygame.locals) ) )

    def render( self ):
        self.renderVariables()
        self.manageConsoleInput()
        self.renderConsoleHistory()

    def renderVariables( self ):
        for i in range( len( self.variables ) ):
            vr = self.variables[i]
            vrRect = vr.get_rect()
            vrRect.center = self.topLeft + pygame.Vector2(vrRect.width/2, i*15)
            self.surface.blit(vr, vrRect)

    def manageConsoleInput( self ):

        if self.focusInput:
            self.renderTextInput()
            keys = pygame.key.get_pressed()

            self.inputCooldown += 1
            if self.inputCooldown >= 8:
                for key in self.keyObjs:
                    if keys[ vars(pygame.locals)[key] ] and len( key ) == 3:
                        self.consoleInput += key[2]
                        self.inputCooldown = 0
                if  keys[ pygame.K_SPACE ]:
                    self.consoleInput += " "
                    self.inputCooldown = 0
                elif keys[ pygame.K_BACKSPACE ] and len(self.consoleInput) >= 1:
                    self.consoleInput = self.consoleInput.rstrip(self.consoleInput[-1])
                    self.inputCooldown = 0
                elif keys[ pygame.K_RETURN ]:
                    newText = self.font.render( self.consoleInput,
                                                True, (255, 255, 255))
                    self.consoleHistory.append( newText  )
                    try:
                        func = consoleFunc[ self.consoleInput.split(" ")[0] ]
                        func( self.consoleInput, self )
                    except:
                        pass
                    
                    self.consoleInput = ""
                    self.inputCooldown = 0

    def renderTextInput( self ):

        s = pygame.Surface( self.inputSize )  
        s.set_alpha(128)                
        s.fill((11, 14, 20))

        inputLabel = self.font.render(self.consoleInput, True, (255, 255, 255)) 
        inputLabelRect = inputLabel.get_rect()
        inputLabelRect.center = ( 5+inputLabelRect.width/2, 2+inputLabelRect.height/2 )
        s.blit( inputLabel, inputLabelRect )
        self.surface.blit(s, self.inputPos ) 

    def renderConsoleHistory( self ):
        for i in range( len( self.consoleHistory ) ):
            msg = self.consoleHistory[ len(self.consoleHistory) - 1 - i]
            msgRect = msg.get_rect()
            msgRect.center = self.bottomLeft + pygame.Vector2(msgRect.width/2, -i*18)
            self.surface.blit(msg, msgRect)

def filterKeysfromCons( k ):
    return k[:2] ==  "K_"