import pygame, random
from spaceship import Spaceship
from obstacle import Obstacle
from obstacle import grid
from alien import Alien
from laser import Laser
from alien import MysteryShip


class Game:

    def __init__(self, screen_width, screen_height, offset):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset))
        self.obstacles = self.create_obstacles()
        self.aliens_group = pygame.sprite.Group()
        # self.create_aliens(2,3)
        self.aliens_direction = 1
        self.alien_lasers_group = pygame.sprite.Group()
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.lives = 3
        self.run = True
        self.score = 0
        self.highscore = 0
        self.explosion_sound = pygame.mixer.Sound("Sounds/explosion.ogg")
        self.load_highscore()
        self.level = 5
        self.max_levels = 5
        self.flag = True
        self.setup_level()
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width + self.offset - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles

    def create_aliens(self, rows, cols):
        for row in range(rows):
            for column in range(cols):
                x = 75 + column * 55
                y = 110 + row * 55

                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1

                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)

    def move_aliens(self):
        self.aliens_group.update(self.aliens_direction)

        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width + self.offset / 2:
                self.aliens_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= self.offset / 2:
                self.aliens_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot_laser(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
            self.alien_lasers_group.add(laser_sprite)

    def create_mystery_ship(self):
        self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))

    def check_for_collisions(self):
        # Spaceship
        if self.spaceship_group.sprite.lasers_group:
            for laser_sprite in self.spaceship_group.sprite.lasers_group:

                aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True)
                if aliens_hit:
                    self.explosion_sound.play()
                    for alien in aliens_hit:
                        self.score += alien.type * 100
                        self.check_for_highscore()
                        laser_sprite.kill()

                if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    self.score += 500
                    self.explosion_sound.play()
                    self.check_for_highscore()
                    laser_sprite.kill()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

        # Alien Lasers
        if self.alien_lasers_group:
            for laser_sprite in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
        if not self.aliens_group:
            self.next_level()
        if self.aliens_group:
            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()

    def create_aliens2(self):
        for row in range(0, 5):
            for column in range(0, 5):
                x = 75 + column * 55
                y = 110 + row * 55
                if column == 0 or column == 4:
                    alien_type = 1
                elif row == 4:
                    alien_type = 1
                elif row == 0:
                    alien_type = 1
                else:
                    if row == 2 and (column != 0 or column != 4):
                        alien_type = 3
                    else:
                        alien_type = 2

                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)

    def create_aliens4(self):
        num_rows = 5
        middle_row = num_rows // 2

        for row in range(num_rows):
            num_aliens = num_rows - abs(middle_row - row)
            row_width = num_aliens * 55
            row_start_x = (self.screen_width - row_width) // 2

            for col in range(num_aliens):
                x = row_start_x + col * 55
                y = 110 + row * 55

                if row == 0 or row == num_rows - 1:
                    alien_type = 1
                elif row == middle_row:
                    alien_type = 3
                else:
                    alien_type = 2

                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)

    def create_aliens3(self):
        num_rows = 3
        middle_row = num_rows // 2

        for row in range(num_rows):
            num_aliens = num_rows - abs(middle_row - row)
            row_width = num_aliens * 55
            row_start_x = (self.screen_width - row_width) // 2

            for col in range(num_aliens):
                x = row_start_x + col * 55
                y = 110 + row * 55

                if row == 0 or row == num_rows - 1:
                    alien_type = 2
                elif row == middle_row:
                    alien_type = 3
                else:
                    alien_type = 3

                alien = Alien(alien_type, x + self.offset - 350 / 2, y)
                self.aliens_group.add(alien)
                alien2 = Alien(alien_type, x + self.offset + 350 / 2, y)
                self.aliens_group.add(alien2)
        for row in range(2):
            for column in range(11):
                x = 90 + column * 55
                y = 290 + row * 55

                alien_type = 1

                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)

    def create_aliens5(self):
        num_rows = 7
        num_aliens_in_top_row = 5
        alien_type = 3

        for row in range(num_rows):
            num_aliens_in_row = num_aliens_in_top_row - 2 * row
            x_start = 0 + row * 55
            x_start2 = 330 + row * 55
            x_start3 = 165 + row * 55
            y = 90 + row * 55
            y2 = 280 + row * 55

            for column in range(num_aliens_in_row):
                x = x_start + column * 55
                x2 = x_start2 + column * 55
                x3 = x_start3 + column * 55
                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)
                alien2 = Alien(alien_type, x2 + self.offset / 2, y)
                self.aliens_group.add(alien2)
                alien3 = Alien(alien_type, x3 + self.offset / 2, y2)
                self.aliens_group.add(alien3)

            alien_type -= 1

    def setup_level(self):
        self.aliens_group.empty()  # reseting the game here
        if self.level == 1:
            self.create_aliens(rows=4, cols=3)
        elif self.level == 2:
            self.create_aliens2()
        elif self.level == 3:
            self.create_aliens3()
        elif self.level == 4:
            self.create_aliens4()
        elif self.level == 5:
            self.create_aliens5()
        else:
            self.game_over()
        self.flag = True

    def next_level(self):
        self.level += 1

        if self.level <= self.max_levels:
            if (self.score >= 1900 and self.lives <= 4):
                self.lives += 1
                self.score -= 1900
            self.setup_level()
        else:
            # Game completed all levels, you can add a game over or victory screen here
            self.game_over()
            pass

    def game_over(self):
        self.run = False

    def reset(self):
        self.run = True
        self.lives = 3
        self.level = 1
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.setup_level()
        self.mystery_ship_group.empty()
        self.obstacles = self.create_obstacles()
        self.score = 0

    def check_for_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))

    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            self.highscore = 0