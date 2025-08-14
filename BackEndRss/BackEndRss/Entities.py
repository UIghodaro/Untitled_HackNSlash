import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up' : False, 'down' : False, 'left': False, 'right' : False}    #To keep track of what collisions are currently happening

        self.action = ''    #What the character is currently doing
        self.anim_offset = (-3, -3)   #This is as sometimes the animation may be larger than the player hitbox
        self.flip = False       #Characters can turn around lmfao
        self.set_action('idle')     #I love homogeneity
        self.movementModifier = 1.5
        
    #Creating a rect for the entity for the sake of collisions
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    #This is intended for when it comes to changing animations
    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()
        
    def update(self, tilemap, movement = (0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1]) #index 0 is x-axis, index 1 is y-axis
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        if movement[0] > 0: 
            self.flip = False
        if movement[0] < 0:
            self.flip = True
    
        self.pos[0] += frame_movement[0]*self.movementModifier
        
        entity_rect = self.rect()
        for rect in tilemap.physics_rect_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
            
        self.pos[1] += frame_movement[1]
        #As above, but on the y axis
        entity_rect = self.rect()
        for rect in tilemap.physics_rect_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        
        #Uses current movement press in place of velocity to determine whether to flip or not, which is intuitive but sucks for me
        
            
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
        self.animation.update()
        
    def render(self, surf, offset = (0, 0)):
        surf.blit(pygame.transform.flip(self.animation.img(), self.flip, False), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))

class Player(PhysicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0
        self.counter = 0
        self.current_jumps = 0
        self.max_jump = 200
        self.dash = False
        self.reDash = False
    
    def update(self, tilemap, movement = (0, 0)):
        super().update(tilemap, movement=movement)
        
        self.air_time += 1
        self.counter += 1

    
        if movement[0] != 0:
            if self.dash:
                if self.counter < 5:
                    self.movementModifier = 25
                elif self.counter > 60:
                    self.dash = False
                else:
                    self.movementModifier = 4
            else:
                self.counter = 0
                
        else:
            self.movementModifier = 1.5
            self.dash = False
            self.counter = 0
            
        if self.collisions['down']:
            self.air_time = 0
            self.current_jumps = 0
        
        
        if self.air_time > 4:
            self.set_action('jump')
        elif movement[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')