from sys import exit
import random
import pygame
import string

pygame.init()

# Game default settings
pygame.display.set_caption("Awesome-Mix Greed")  # Set the display header
icon = pygame.image.load("greed.png")  # load the game icon image
pygame.display.set_icon(icon)  # set the display icon
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# OTHER VARIABLES
rand = random.randint(10, 20)  # random integer between 10 and 20
letters = list(string.ascii_letters)  # random shapes for our kittens
colors = [(100, random.randint(10, 255), random.randint(10, 255)) for i in range(rand)]

# GLOBAL variables
width = 600
height = 400


class Background:
    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))  # Set the display size (width, height)
        self.text = font.render("Game Over!!!",  False, (255, 100, 255))
        self.rect = self.text.get_rect(center=(width / 2, height / 2))

    def render(self):
        self.screen.fill("Black")

    def done(self):
        self.screen.fill("Gray")
        Score().display()
        # self.screen.blit(self.text, self.rect)


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 20)
        self.image = self.font.render(f"Score: {int(director.score)}", False, "White")
        self.rect = self.image.get_rect(topleft=(5, 5))

    def display(self):
        background.screen.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font("fonts/space_game_icons.ttf", 40)
        self.image = self.font.render('#', False, (255, 255, 255))  # create the Player image
        self.rect = self.image.get_rect(midbottom=(300, 400))  # Place the player at the center of the screen
        self.rect.width = 20
        self.rect.height = 20
        self.x = 0
        self.y = 0

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.y = 0
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.y = 0

        # Rules to ensure the player doesn't run out of the screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= width - 5:
            self.rect.right = width - 5


class Kitten(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 40
        self.font = pygame.font.Font("fonts/space_game_icons.ttf", self.size)
        self.image = self.font.render(random.choice(letters), False, random.choice(colors))
        self.pos_x = random.randrange(50, width - 50)
        self.pos_y = random.randrange(50, 200)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.point = 100

    def update(self):
        self.rect.y += 1
        if pygame.sprite.spritecollide(player.sprite, kittens, True):
            director.update(self.point)
            self.kill()


class Rock(Kitten):
    def __init__(self):
        super().__init__()
        self.size = 20
        self.font = pygame.font.Font("fonts/soldiers.ttf", self.size)
        self.image = self.font.render(random.choice(letters), False, "Red")
        self.point = -100

    def update(self):
        self.rect.y += 1
        if pygame.sprite.spritecollide(player.sprite, rocks, True):
            director.update(self.point)
            self.kill()


class BigKitten(Kitten):
    def __init__(self):
        super().__init__()
        self.size = 80
        self.font = pygame.font.Font("fonts/space_game_icons.ttf", self.size)
        self.image = self.font.render(random.choice(letters), False, "white")
        self.rect.height = 50
        self.rect.width = 50
        self.point = 500

    def update(self):
        self.rect.y += 2
        if pygame.sprite.spritecollide(player.sprite, big_kittens, True):
            director.update(self.point)
            self.kill()


class BigRock(BigKitten):
    def __init__(self):
        super().__init__()
        self.image = self.font.render(random.choice(letters), False, "red")
        self.point = -700

    def update(self):
        self.rect.y += 2
        if pygame.sprite.spritecollide(player.sprite, big_rocks, True):
            director.update(self.point)
            self.kill()


class Director:
    def __init__(self):
        self.running = True
        self.score = 0

    def update(self, point):
        if self.running:
            self.score += point

    def display(self):
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # Draw and display all game graphics
        background.screen.fill("Black")  # background colour
        Score().display()  # score
        player.draw(background.screen)  # player
        rocks.draw(background.screen)  # rocks
        kittens.draw(background.screen)  # small kittens
        big_kittens.draw(background.screen)  # Big kittens
        big_rocks.draw(background.screen)  # Big rocks

        # Update the changes made to the drawings
        big_kittens.update()
        big_rocks.update()
        kittens.update()
        rocks.update()
        if self.score <= 1000:
            self.score += 0.1
        elif self.score >= 10000:
            self.score += 0.5
        elif self.score > 15000:
            self.score += 1

    def play(self):
        # Run the game until the user quits
        while self.running:
            for event in pygame.event.get():  # loop through all events
                if event.type == pygame.QUIT:  # check if user click close button
                    pygame.quit()
                    exit()  # terminate the loop

                if event.type == ADDROCKS:
                    new_rocks = Rock()
                    rocks.add(new_rocks)

                elif event.type == ADDKITTENS:
                    new_kittens = Kitten()
                    kittens.add(new_kittens)

                elif event.type == ADDBIGKITTEN:
                    new_big_kittens = BigKitten()
                    big_kittens.add(new_big_kittens)

                elif event.type == ADDBIGROCK:
                    new_big_rocks = BigRock()
                    big_rocks.add(new_big_rocks)

            director.display()
            director.over()

            pygame.display.flip()  # Update the changes made to the screen
            clock.tick(45)

    def over(self):
        if self.score <= 0:
            self.score = 0
            background.done()


background = Background()
director = Director()

# KITTENS GROUP
kittens = pygame.sprite.Group()
for i in range(rand):
    kittens.add(Kitten())

# BIG KITTENS
big_kittens = pygame.sprite.GroupSingle()
big_kittens.add(big_kittens)

# BIG ROCKS
big_rocks = pygame.sprite.GroupSingle()
big_rocks.add(big_rocks)

# ROCKS GROUP
rocks = pygame.sprite.Group()
for i in range(rand - 5):  # STart the game with lesser rocks
    rocks.add(Rock())

# PLAYER GROUP
player = pygame.sprite.GroupSingle()
player.add(Player())

# Add new rocks every 700 milliseconds
ADDROCKS = pygame.USEREVENT + 1
pygame.time.set_timer(ADDROCKS, 700)

# Spawn new kittens every 300 milliseconds
ADDKITTENS = pygame.USEREVENT + 2
pygame.time.set_timer(ADDKITTENS, 300)

# Spawn big kittens and big rocks
ADDBIGKITTEN = pygame.USEREVENT + 3
pygame.time.set_timer(ADDBIGKITTEN, random.randint(9000, 15000))

# Spawn big kittens and big rocks
ADDBIGROCK = pygame.USEREVENT + 4
pygame.time.set_timer(ADDBIGROCK, random.randint(9000, 12000))

director.play()
