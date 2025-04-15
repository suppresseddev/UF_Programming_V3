import pygame
from random import randint, random
import math
class Mole (pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.x = 0
        self.y = 0
        self.rect = images[0].get_rect()
        self.time = 0
        self.images = images
        self.images_frame = 0
    def draw(self, screen):
        self.time += 1
        if self.time < 20:
            self.images_frame = 0
        elif self.time < 40:
            self.images_frame = 1
        elif self.time < 60:
            self.images_frame = 2
        elif self.time < 80:
            self.images_frame = 3
        else:
            self.time = 0
        screen.blit(self.images[self.images_frame], (self.rect.x + 3, self.rect.y + 3))
    def new_position(self):
        #Grid is 20 (x) by 16 (y)
        self.rect.x = randint(0, 19) * 32
        self.rect.y = randint(0, 15) * 32
def mouse_over(object, cur_pos):
    return object.rect.collidepoint(cur_pos)
def rainbow_colors():
    moment = pygame.time.get_ticks() / 360
    red = abs(math.sin(moment + 1) * 255)
    green = abs(math.sin(moment + 2) * 255)
    blue = abs(math.sin(moment + 3) * 255)
    return (red, green, blue)
def draw_grid(screen):
    screen.fill((0, 0, 0))
    for col in range(1, 21):
        pygame.draw.line(screen, rainbow_colors(), ((col * 32), 0), ((col * 32), 512))
    for row in range(1, 17):
        pygame.draw.line(screen, rainbow_colors(), (0, (row * 32)), (640, (row * 32)))
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_images = [pygame.image.load('mole_step1.png'), pygame.image.load('mole.png'), pygame.image.load('mole_step2.png'), pygame.image.load('mole.png')]
        mole_object = Mole(mole_images)
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if mouse_over(mole_object, pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0] == 1:
                            print("The mole has been clicked!")
                            mole_object.new_position()
            screen.fill("black")
            draw_grid(screen)
            mole_object.draw(screen)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
