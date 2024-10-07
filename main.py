import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from scoreboard import *
from gameover import *

def main():
    pygame.init()

    time = pygame.time.Clock()
    dt = 0
    active = 0
    game_over = 1
    game_state = active

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    Scoreboard.containers = (drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, shots)
    asteroid_field = AsteroidField()
    scoreboard = Scoreboard(screen, 36, (255, 255, 255))

    while game_state == active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                game_state = game_over
            
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    shot.kill()
                    scoreboard.increase(asteroid.score_value)
                    asteroid.split()
        
        for entity in drawable:
            entity.draw(screen, game_state)

        pygame.display.flip()
        time.tick(60) #60 fps
        dt = time.tick(60) / 1000

    while game_state == game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))




if __name__ == "__main__":
    main()