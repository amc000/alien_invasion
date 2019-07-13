import sys, pygame, game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    # Initialize game and create window object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # make a ship, a group to store bullets in, and one to store aliens in.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # Make an alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)

        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
