# Reshma Gudla
# Space Invaders

# Directions
"""Use the arrow keys to move left and right,
use the space bar to shoot. Hide behind the
shields if needed, and get bonus points
by hitting the invader that flies across
the top of the screen occasionally."""

import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
CRIMSON = (220, 20, 60)
DARKORANGE = (255, 140, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
TOMATO = (255, 99, 71)
BLUE = (0, 255, 255)

first_block_list = pygame.sprite.Group()

second_block_list = pygame.sprite.Group()

third_block_list = pygame.sprite.Group()

fourth_block_list = pygame.sprite.Group()

fifth_block_list = pygame.sprite.Group()

bonus_block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

player_bullet_list = pygame.sprite.Group()

enemy_bullet_list = pygame.sprite.Group()

barrier_block_list_left = pygame.sprite.Group()

barrier_block_list_left_middle = pygame.sprite.Group()

barrier_block_list_right_middle = pygame.sprite.Group()

barrier_block_list_right = pygame.sprite.Group()

player_list = pygame.sprite.Group()

score = 0

lives = 3


class Fleet:
    """This class groups all the enemies together as a 'fleet'."""
    
    def __init__(self, x_speed, y_speed):
        '''This function establishes the variables used in the rest of the Class.

        Arguments:
        x_speed = the horizontal speed 
        y_speed = the vertical speed
        '''
        
        self.x_speed = x_speed
        self.enemy_list = []
        self.y_speed = y_speed

class Enemy(pygame.sprite.Sprite):
    """This class defines the characteristics of a SINGLE enemy."""
    
    def __init__(self, color, width, height, x, y, f):
        '''This function establishes the variables used in the rest of the Class.

        Arguments:
        color = the color of the enemy
        width = the width of the enemy
        height = the height of the enemy
        x = the x coordinate
        y = the y coordinate
        f = the fleet
        '''
        
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fleet = f

    def update(self):
        '''This function moves the enemy.'''
        
        if self.rect.x >= 1000:
            self.rect.x = 0
            self.rect.y += self.fleet.y_speed
            self.rect.x += self.fleet.x_speed
        else:
            self.rect.x += self.fleet.x_speed

    def shoot(self):
        '''This function shoots a bullet from the enemy.'''
        
        return EnemyBullet(self.rect.x, self.rect.y)
        
  
class Player(pygame.sprite.Sprite):
    """This class defines the characteristics of the player."""
    
    def __init__(self, color, width, height, x, y):
        '''This function establishes the variables used in the rest of the Class.

        Arguments:
        color = the color of the enemy
        width = the width of the enemy
        height = the height of the enemy
        x = the x coordinate
        y = the y coordinate
        '''
        
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        
    def changespeed(self, x, y):
        '''This function changes the speed of the player.'''
        
        self.change_x = x
        self.change_y = y
        
    def update(self):
        '''This function allows the player to move.'''
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Barrier(pygame.sprite.Sprite):
    """This class defines the characteristics of a SINGLE barrier."""
    
    def __init__(self, color, width, height, x, y):
        '''This function establishes the variables used in the rest of the Class.

        Arguments:
        color = the color of the enemy
        width = the width of the enemy
        height = the height of the enemy
        x = the x coordinate
        y = the y coordinate
        '''
        
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0

    
class BarrierFleet:
    """This class groups all the barriers together as a 'barrier fleet'."""
    
    for i in range(10):
        x_coor = 150 + (i * 10)
        y_coor = 500 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 650)
        barrier_block_list_left.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 150 + (i * 10)
        y_coor = 500 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 665)
        barrier_block_list_left.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 350 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 650)
        barrier_block_list_left_middle.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 350 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 665)
        barrier_block_list_left_middle.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 550 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 650)
        barrier_block_list_right_middle.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 550 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 665)
        barrier_block_list_right_middle.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 750 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 650)
        barrier_block_list_right.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 750 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 665)
        barrier_block_list_right.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 150 + (i * 10)
        y_coor = 500 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 680)
        barrier_block_list_left.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 350 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 680)
        barrier_block_list_left_middle.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 550 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 680)
        barrier_block_list_right_middle.add(barrier_block)
        all_sprites_list.add(barrier_block)

    for i in range(10):
        x_coor = 750 + (i * 10)
        y_coor = 700 + (i * 10)
        barrier_block = Barrier(WHITE, 15, 15, x_coor, 680)
        barrier_block_list_right.add(barrier_block)
        all_sprites_list.add(barrier_block)


class EnemyBullet(pygame.sprite.Sprite):
    """This class represents an enemy's bullet."""
    
    def __init__(self, x, y):
        '''This function establishes the variables used in the rest of the Class.

        Arguments:
        x = x-coordinate
        y = y-coordinate
        '''
        
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def update(self):
        '''This function moves the bullet.'''
        
        self.rect.y += 10


class PlayerBullet(pygame.sprite.Sprite):
    """This class represents the player's bullet."""
    
    def __init__(self):

        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
        
    def update(self):
        '''This function moves the bullet.'''
        
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()


def make_bonus():
    '''This function makes the flying invader at the top of the screen.'''
    
    global bonus_fleet
    bonus = Enemy(TOMATO, 50, 50, 100, 25, bonus_fleet)
    bonus_fleet.enemy_list.append(bonus)
    fleet.enemy_list.append(bonus)
    bonus_block_list.add(bonus)
    all_sprites_list.add(bonus)


pygame.init()

size = (1000, 900)

screen = pygame.display.set_mode(size)

hit_barrier = pygame.mixer.Sound("barrier.wav")

bad_click_sound = pygame.mixer.Sound("invaderkilled.wav")

player_shoot = pygame.mixer.Sound("shoot.wav")

enemy_shoot = pygame.mixer.Sound("shoot2.wav")

player_killed = pygame.mixer.Sound("playerkilled.wav")

bonus_killed = pygame.mixer.Sound("shipexplosion.wav")

background_position = [-20, -20]

Galaxy = pygame.image.load("galaxy.png").convert()

fleet = Fleet(1, 10)

bonus_fleet = Fleet(5, 0)

barrier_fleet = BarrierFleet()

player = Player(GREEN, 100, 50, 450, 725)

player_list.add(player)

all_sprites_list.add(player)

make_bonus()

for i in range(11):
    x_coor = 25 + (i * 70)
    block = Enemy(CRIMSON, 50, 50, x_coor, 100, fleet)
    fleet.enemy_list.append(block)
    fifth_block_list.add(block)
    all_sprites_list.add(block)

for i in range(11):
    x_coor = 25 + (i * 70)
    block = Enemy(DARKORANGE, 50, 50, x_coor, 200, fleet)
    fleet.enemy_list.append(block)
    fourth_block_list.add(block)
    all_sprites_list.add(block)

for i in range(11):
    x_coor = 25 + (i * 70)
    block = Enemy(DARKORANGE, 50, 50, x_coor, 300, fleet)
    fleet.enemy_list.append(block)
    third_block_list.add(block)
    all_sprites_list.add(block)

for i in range(11):
    x_coor = 25 + (i * 70)
    block = Enemy(GOLD, 50, 50, x_coor, 400, fleet)
    fleet.enemy_list.append(block)
    second_block_list.add(block)
    all_sprites_list.add(block)

for i in range(11):
    x_coor = 25 + (i * 70)
    block = Enemy(GOLD, 50, 50, x_coor, 500, fleet)
    fleet.enemy_list.append(block)
    first_block_list.add(block)
    all_sprites_list.add(block)


pygame.display.set_caption("Space Invaders: Final Project 2018")


done = False

keys_down = 0

clock = pygame.time.Clock()

left_down = False

right_down = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            keys_down += 1
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
                left_down = True
                player.update()
            elif event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
                right_down = True
                player.update()
            elif event.key == pygame.K_SPACE:
                if player_bullet_list.sprites() == []:
                    player_bullet = PlayerBullet()
                    player_shoot.play()
                    player_bullet.rect.x = player.rect.x + 50
                    player_bullet.rect.y = player.rect.y
                    all_sprites_list.add(player_bullet)
                    player_bullet_list.add(player_bullet)

        elif event.type == pygame.KEYUP:
            keys_down -= 1
            if event.key == pygame.K_LEFT:
                if not right_down:
                    player.changespeed(0, 0)
                left_down = False
                player.update()
            elif event.key == pygame.K_RIGHT:
                if not left_down:
                    player.changespeed(0, 0)
                right_down = False
                player.update()
    
    pygame.font.init()
    
    for enemy in fleet.enemy_list:
        num = random.randrange(0, 2500)
        if num == 50 and enemy.alive():
            enemy_bullet = EnemyBullet(enemy.rect.x + 25, enemy.rect.y)
            enemy_shoot.play()
            all_sprites_list.add(enemy_bullet)
            enemy_bullet_list.add(enemy_bullet)

    screen.blit(Galaxy, background_position)

    for bullet in player_bullet_list:
        first_enemy_list = pygame.sprite.spritecollide(bullet, first_block_list, True)
        if first_enemy_list != []:
            bullet.kill()
            score += 10
            bad_click_sound.play()
            
        second_enemy_list = pygame.sprite.spritecollide(bullet, second_block_list, True)
        if second_enemy_list != []:
            bullet.kill()
            score += 10
            bad_click_sound.play()
            
        third_enemy_list = pygame.sprite.spritecollide(bullet, third_block_list, True)
        if third_enemy_list != []:
            bullet.kill()
            score += 20
            bad_click_sound.play()
            
        fourth_enemy_list = pygame.sprite.spritecollide(bullet, fourth_block_list, True)
        if fourth_enemy_list != []:
            bullet.kill()
            score += 20
            bad_click_sound.play()
            
        fifth_enemy_list = pygame.sprite.spritecollide(bullet, fifth_block_list, True)
        if fifth_enemy_list != []:
            bullet.kill()
            score += 30
            bad_click_sound.play()
            
        bonus_player_list = pygame.sprite.spritecollide(bullet, bonus_block_list, True)
        if bonus_player_list != []:
            bullet.kill
            score += 100
            lives += 1
            make_bonus()
            bonus_killed.play()
            
        first_barrier_player = pygame.sprite.spritecollide(bullet, barrier_block_list_left, True)
        if first_barrier_player != []:
            bullet.kill()
            hit_barrier.play()
            
        second_barrier_player = pygame.sprite.spritecollide(bullet, barrier_block_list_left_middle, True)
        if second_barrier_player != []:
            bullet.kill()
            hit_barrier.play()
            
        third_barrier_player = pygame.sprite.spritecollide(bullet, barrier_block_list_right_middle, True)
        if third_barrier_player != []:
            bullet.kill()
            hit_barrier.play()
            
        fourth_barrier_player = pygame.sprite.spritecollide(bullet, barrier_block_list_right, True)
        if fourth_barrier_player != []:
            bullet.kill()
            hit_barrier.play()
            
        if first_block_list.sprites() == [] and second_block_list.sprites() == [] and third_block_list.sprites() == [] and fourth_block_list.sprites() == [] and fifth_block_list.sprites() == []:
            highscore = open("spaceinvadershighscore.txt", "r") 
            if all(int(value) < score for value in highscore):
                high_score_font = pygame.font.SysFont('Comic Sans MS', 30)
                text_surface_high = score_font.render('Your high score is ' + str(score) + "!!", False, WHITE)
                screen.blit(text_surface_high, (650, 825))
            highscore.close()
            highscore = open("spaceinvadershighscore.txt", "a")
            highscore.write(str(score) + "\n")
            highscore.close()
            done = True
            
        bullet_colllision = pygame.sprite.spritecollide(bullet, enemy_bullet_list, True)
        if bullet_colllision != []:
            bullet.kill()


    for enemy_bullet in enemy_bullet_list:
        first_barrier = pygame.sprite.spritecollide(enemy_bullet, barrier_block_list_left, True)
        if first_barrier != []:
            enemy_bullet.kill()
            hit_barrier.play()
            
        second_barrier = pygame.sprite.spritecollide(enemy_bullet, barrier_block_list_left_middle, True)
        if second_barrier != []:
            enemy_bullet.kill()
            hit_barrier.play()
            
        third_barrier = pygame.sprite.spritecollide(enemy_bullet, barrier_block_list_right_middle, True)
        if third_barrier != []:
            enemy_bullet.kill()
            hit_barrier.play()
            
        fourth_barrier = pygame.sprite.spritecollide(enemy_bullet, barrier_block_list_right, True)
        if fourth_barrier != []:
            enemy_bullet.kill()
            hit_barrier.play()
            
        kill_player = pygame.sprite.spritecollide(enemy_bullet, player_list, True)
        if kill_player != []:
            lives -= 1
            enemy_bullet.kill()
            player_killed.play()
            if lives > 0:
                player = Player(GREEN, 100, 50, 450, 725)
                all_sprites_list.add(player)
                player_list.add(player)
                
            if lives == 0:
                highscore = open("spaceinvadershighscore.txt", "r") 
                if all(int(value) < score for value in highscore):
                    high_score_font = pygame.font.SysFont('Comic Sans MS', 30)
                    text_surface_high = score_font.render('Your high score is ' + str(score) + "!!", False, WHITE)
                    screen.blit(text_surface_high, (650, 825))
                highscore.close()
                highscore = open("spaceinvadershighscore.txt", "a")
                highscore.write(str(score) + "\n")
                highscore.close()
                done = True

               
    lives_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = lives_font.render('Lives: ' + str(lives), False, WHITE)
    screen.blit(text_surface, (800, 30))

    score_font = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = score_font.render('Score: ' + str(score), False, WHITE)
    screen.blit(textsurface, (30, 825))

    all_sprites_list.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()
    
    if lives == 0:
        pygame.time.delay(3000)

    if first_block_list.sprites() == [] and second_block_list.sprites() == [] and third_block_list.sprites() == [] and fourth_block_list.sprites() == [] and fifth_block_list.sprites() == []:
        pygame.time.delay(3000)
        
    clock.tick(60)


pygame.quit()
