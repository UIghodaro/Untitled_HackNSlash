import pygame

class Attack:
    def __init__(self, pos, owner, damage, lifetime = 300):
        self.owner = owner
        self.damage = damage
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = lifetime
        self.rect = self.image.get_rect(center=pos)
    
    def hack():
        return
    def slash():
        return
    def beam():
        return
    
    
    def update(self):
        # Despawn after lifetime ends
        if pygame.time.get_ticks() - self.spawn_time > self.lifetime:
            self.kill()
