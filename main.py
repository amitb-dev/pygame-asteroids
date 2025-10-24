import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField()

    score = 0

    try:
        font = pygame.font.Font(None, 36) # Pygame's default font
    except pygame.error:
        print("Warning: Could not load default font.")
        font = None

    GAME_STATE_PLAYING = "playing"
    GAME_STATE_OVER = "game_over"
    state = GAME_STATE_PLAYING # Start the game in the playing state

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.isCollide(player):
                print("Game over!")
                running = False
                break
            for bullet in shots:
                if asteroid.isCollide(bullet):
                    score += asteroid.get_score()
                    asteroid.split()
                    bullet.kill()
                    break

        screen.fill("Black")

        for entity in drawable:
            entity.draw(screen)

        if font:
            text_surface = font.render(f"Score: {score}", True, "white")
            # Draw it in the top left corner
            screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
