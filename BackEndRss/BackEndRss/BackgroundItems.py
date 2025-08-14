import random

class BackGround:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth
        
    #def update(self):
        
    def render(self, surf, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        #See below, a really smart way of creating looping structures using modular arithmetic (bless set theory)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

#This class stores all of our clouds
class Mountains:
    def __init__(self, Item_images, count=7):
        self.Items = []
        
        for i in range(count):
            chosenImage = random.choice(Item_images)
            
            #Instantiates 16 cloud variables at random places in the screen with random speeds from the cloud_images folder (for cloud variants) randomly
            self.Items.append(BackGround((random.random() * 99999, 240), chosenImage, random.random() * 0.05 + 0.05, (random.random() * 0.6 + 0.2) % chosenImage.get_height()))
            
        self.Items.sort(key=lambda x: x.depth)     #Sorts all clouds based on their depth
            
    #def update(self):
    #    for Item in self.Mountains:
    #        Item.update()
            
    def render(self, surf, offset=(0,0)):
        for Item in self.Items:
            Item.render(surf, offset=offset)