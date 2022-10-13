import pygame
import random

pygame.init()

width = 800
height = 600
FPS = 60
distance = 10
speed = 5
score = 0
clock = pygame.time.Clock()
lives = 5

font = pygame.font.SysFont("comicsansms", 30)

screen = pygame.display.set_mode((width, height))

gray = (150, 150, 150)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.display.set_caption("Chytni pivo!")

pygame.mixer.music.load("sound/background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

sound_pick = pygame.mixer.Sound("sound/pick.mp3")
sound_pick.set_volume(0.5)

sound_crash = pygame.mixer.Sound("sound/crash3.mp3")
sound_crash.set_volume(0.5)

image_hands = pygame.image.load("images/hands1.png")
rect_image_hands = image_hands.get_rect()
rect_image_hands.left = 0
rect_image_hands.top = height // 2

image_beer = pygame.image.load("images/beer1.png")
rect_image_beer = image_beer.get_rect()
rect_image_beer.right = width - 20
rect_image_beer.top = height // 2

image_background = pygame.image.load("images/background1.png")
rect_image_background = image_background.get_rect()
rect_image_background.center = width//2, height//2 + 20

font_header = font.render("Chytni pivo!", True, white)
font_header_rect = font_header.get_rect()
font_header_rect.center = width // 2, 25

font_continue = font.render("Jestli chceš pokračovat, tak klikni myší.", True, black)
font_continue_rect = font_continue.get_rect()
font_continue_rect.center = width // 2, height // 2 + 80

letscontinue = True

while letscontinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            letscontinue = False

    event = pygame.key.get_pressed()
    if event[pygame.K_UP] and rect_image_hands.top > 80:
        rect_image_hands.y -= distance
    elif event[pygame.K_DOWN] and rect_image_hands.bottom < height:
        rect_image_hands.y += distance

    font_score = font.render(f"Skore: {score}", True, white)
    font_score_rect = font_score.get_rect()
    font_score_rect.centery = 25
    font_score_rect.centerx = 80

    font_lives = font.render(f"Životy: {lives}", True, white)
    font_lives_rect = font_lives.get_rect()
    font_lives_rect.centery = 25
    font_lives_rect.centerx = width - 80

    # screen.fill(gray)
    screen.blit(image_background, rect_image_background)

    randomY = random.randint(100, height - 50)

    if rect_image_hands.colliderect(rect_image_beer):
        rect_image_beer.top = randomY
        rect_image_beer.right = width
        score += 1
        speed += 0.5
        sound_pick.play()

    if rect_image_beer.centerx < 0:
        rect_image_beer.top = randomY
        rect_image_beer.right = width
        lives -= 1
        sound_crash.play()

    if lives <= 0:

        font_endgame = font.render(f"Konec hry, dosáhl si skore: {score}", True, black)
        font_endgame_rect = font_endgame.get_rect()
        font_endgame_rect.center = width // 2, height // 2 -5

        screen.blit(font_endgame, font_endgame_rect)
        screen.blit(font_continue, font_continue_rect)
        pygame.display.update()

        pause = True
        while pause:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    lives = 5
                    speed = 5
                    rect_image_hands.y = height // 2
                    pause = False
                elif event.type == pygame.QUIT:
                    pause = False
                    letscontinue = False

    rect_image_beer.right -= speed

    pygame.draw.rect(screen, black, (0, 0, 800, 57), 0,)
    screen.blit(image_hands, rect_image_hands)
    screen.blit(font_header, font_header_rect)
    screen.blit(image_beer, rect_image_beer)
    screen.blit(font_score, font_score_rect)
    screen.blit(font_lives, font_lives_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
