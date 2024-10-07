import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init

    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS, shots)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game Over!")
                exit()
            
            for shot in shots:
                if shot.check_collision(asteroid) == True:
                    shot.kill()
                    asteroid.split()
        
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        time.tick(60) #60 fps
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()