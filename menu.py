import pygame ,sys
from button import Button
import random
from game import Game

pygame.init()
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50
SCREEN = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
pygame.display.set_caption("Menu")


def get_font(size):
    return pygame.font.Font("Font/monogram.ttf", size)

def play():
    SCREEN.fill((0, 0, 0))

    OFFSET = 50

    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2

    GREY = (29, 29, 27)
    YELLOW = (243, 216, 63)

    font = pygame.font.Font("Font/monogram.ttf", 40)
    # level_surface = font.render("LEVEL 0" + str(a), False, YELLOW)
    game_over_surface = font.render("GAME OVER", False, YELLOW)
    score_text_surface = font.render("SCORE", False, YELLOW)
    highscore_text_surface = font.render("HIGH-SCORE", False, YELLOW)

    clock = pygame.time.Clock()

    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

    SHOOT_LASER = pygame.USEREVENT
    pygame.time.set_timer(SHOOT_LASER, 300)

    MYSTERYSHIP = pygame.USEREVENT + 1
    pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

    game_started = False

    while True:
        # Checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Check for key presses
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == SHOOT_LASER and game.run:
                game.alien_shoot_laser()

            if event.type == MYSTERYSHIP and game.run:
                game.create_mystery_ship()
                pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and game.run == False:
                game.reset()

        # Updating
        if game.run:
            game.spaceship_group.update()
            game.move_aliens()
            game.alien_lasers_group.update()
            game.mystery_ship_group.update()
            game.check_for_collisions()

        # Drawing
        SCREEN.fill(GREY)

        # UI
        pygame.draw.rect(SCREEN, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(SCREEN, YELLOW, (25, 730), (775, 730), 3)

        if game.run:
            level_surface = font.render("LEVEL 0" + str(game.level), False, YELLOW)
            SCREEN.blit(level_surface, (570, 740, 50, 50))

        else:
            SCREEN.blit(game_over_surface, (570, 740, 50, 50))

        x = 50
        for life in range(game.lives):
            SCREEN.blit(game.spaceship_group.sprite.image, (x, 745))
            x += 50

        SCREEN.blit(score_text_surface, (50, 15, 50, 50))
        formatted_score = str(game.score).zfill(5)
        score_surface = font.render(formatted_score, False, YELLOW)
        SCREEN.blit(score_surface, (50, 40, 50, 50))
        SCREEN.blit(highscore_text_surface, (550, 15, 50, 50))
        formatted_highscore = str(game.highscore).zfill(5)
        highscore_surface = font.render(formatted_highscore, False, YELLOW)
        SCREEN.blit(highscore_surface, (625, 40, 50, 50))

        if (game.flag == True):
            level_load = font.render("LEVEL 0" + str(game.level), False, YELLOW)
            SCREEN.blit(level_load, (center_x - level_load.get_width() / 2, center_y - level_load.get_height() / 2))
            game.flag = False
            # pygame.time.delay(3000)

        game.spaceship_group.draw(SCREEN)
        game.spaceship_group.sprite.lasers_group.draw(SCREEN)
        for obstacle in game.obstacles:
            obstacle.blocks_group.draw(SCREEN)
        game.aliens_group.draw(SCREEN)
        game.alien_lasers_group.draw(SCREEN)
        game.mystery_ship_group.draw(SCREEN)

        pygame.display.update()
        clock.tick(60)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        LOGIN_BUTTON = Button(image=None, pos=(400, 460),
                              text_input="LOGIN", font=get_font(75), base_color="White", hovering_color="Green")

        OPTIONS_BACK = Button(image=None, pos=(400, 500),
                              text_input="BACK", font=get_font(50), base_color="White", hovering_color="Green")

        LOGIN_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        LOGIN_BUTTON.update(SCREEN)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    screen_info = pygame.display.Info()
    BG = pygame.image.load("Untitled design.png")
    BG = pygame.transform.scale(BG, (screen_info.current_w, screen_info.current_h))
    #SCREEN.blit(BG, (0,0))
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 400))

        PLAY_BUTTON = Button(image=None, pos=(400, 450),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=None, pos=(395, 500),
                                text_input="LOGIN", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=None, pos=(400, 550),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()