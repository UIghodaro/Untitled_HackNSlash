#Vision for the game: I'm imagining, naturally, a hack 'n' slash, but with the idea of dual wielding (thanks Freda) at its core.  
#Players will be required to use 2 controls for attacking and only those 2, either j and k (fully keyboard) or left and right click (semi keyboard)
#Left hand would be more accustomed for blunt force damage and simply making the opponent feel pain (screen stop n shake on left hit please). While the aim is to entice the player into becoming a worse person in favour of satisfaction, it will be involved in combos and deal more damage to armoured enemies.
#Right hand would be more accustomed for slicing and directly killing the opponent. The aim is to make this feel less satisfying, but be amazing for combos and wiping out small enemies
#Movement needs to feel nice, acceleration and Shift (dodge + sprint in one) combined with weapon use for launching can achieve this... Not too convoluted though

#I have a vision, will it be hard though? Fuck yeah TT-TT
#Tasks: 
#1. Get a basic screen and player moving that doesn't feel ass (scroll and collisions).      -> Done!!!
#2. Get basic assets going                                                                   -> Not done but moving on
#3. Begin implementing game mechanics as above, make test dummy enemy
#4. Finish mechanics and create a sandbox to create enemy AI and test game mechanics (AFTER THIS STAGE DON'T ADD ANYMORE MECHANICS. NO DEVELOPER HELL.)
#5. Begin to create the levels, aim is 3, 1 tutorial, 2 accustoming, 3 a final boss, but this can be jank for now, focus on screen switches
#6. Build the final boss and then add finish to the game to make it feel higher quality and cleaner
#7. Mini story, then message jake from GameWizards (iirc???), by this point you're probably feeling prouder than ever

#Let's see how this goes. 1 is completable on the flight lowkey (barely)
#IT WAS NOT COMPLETED ON THE FLIGHT AHAHAHAHAHA

import sys
import pygame

from BackEndRss.Utils import load_image, load_images, Animation
from BackEndRss.Entities import Player, PhysicsEntity
from BackEndRss.Mapping import Tilemap
from BackEndRss.BackgroundItems import BackGround, Mountains

RENDER_SCALE = 2.0

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Untitled Hack \'n\' slash')
        self.screen = pygame.display.set_mode((1920, 1080))
        self.display = pygame.Surface((960, 540))
        
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        
        self.assets = {
            'alpha': load_images('Blocks/Alpha'),
            'mountains': load_images('BckGrndRss/Mountains'),
            #'grass': load_images('tiles/grass'),
            #'large_decor': load_images('tiles/large_decor'),
            #'stone': load_images('tiles/stone'),
            'player': load_image('Entities/Player/Alpha/AlphaMC.png'),
            'player/idle': Animation(load_images('Entities/Player/Alpha'), img_dur=10),
            'player/run': Animation(load_images('Entities/Player/Alpha'), img_dur=7),
            'player/jump': Animation(load_images('Entities/Player/Alpha')),
        }
        
        
        self.scroll = [0, 0]
        self.backGround = Mountains(self.assets['mountains'], count = 16)
        self.player = Player(self, (50,50), (32,32))
        self.tilemap = Tilemap(self, tile_size=32)
        try:
            self.tilemap.load('map.json')
        except FileNotFoundError:
            print("Map.json not found")
            pass
        
    def run(self):
        while True:
            self.display.fill((25, 25, 25))
            
            #????
            #This is magic btw don't ask me what the fuck this is
            #It controls the camera, full stop
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 3 - self.scroll[0]) / 20
            self.scroll[1] += (self.player.rect().centery - self.display.get_width() / 2.8 - self.scroll[1]) / 20
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            #self.backGround.update()
            self.backGround.render(self.display, offset = render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)
            
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))    #Uses a boolean equation such that if the left and right movements are pressed at the same time, the player stops moving
            self.player.render(self.display, offset = render_scroll)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                #if event.type == pygame.MOUSEBUTTONDOWN:
                    
                #if event.type == pygame.MOUSEBUTTONUP:
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    
                #self.player.velocity[0] += (self.movement[1] - self.movement[0]) * min(7, self.player.velocity[0]) 
                       
                    if event.key == pygame.K_SPACE:
                        if self.player.current_jumps < self.player.max_jump:
                            self.player.velocity[1] = -3
                            self.player.current_jumps += 1
                            
                    if event.key == pygame.K_LSHIFT:
                            self.player.dash = True
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False
            
            pygame.display.update()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(60)

Game().run()