import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}, Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            for s in shots:
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    a.split()
                    s.kill()

        for a in asteroids:
            if player.collides_with(a):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        clock.tick(60)
        dt = clock.tick(60) / 1000.0
        
        pygame.display.flip()
       
        

if __name__ == "__main__":
    main()
0