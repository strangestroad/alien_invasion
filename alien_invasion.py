import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf
from pygame.sprite import Group
from button import Button
def run_game():
     #Initialize game and create a screen object.
    s=Settings()
    pygame.init()
    screen= pygame.display.set_mode((s.screen_width, s.screen_height))
    ship=Ship(s,screen)
    pygame.display.set_caption("Alien Invasion")

    #Make the Play button
    play_button=Button(s,screen,"Play")

    #Make a group to store bullets,aliens in
    bullets=Group()
    aliens=Group()

    #Create the fleet of aliens
    gf.create_fleet(s,screen,ship,aliens)

    #Create an instance to store game statistics and score
    stats=GameStats(s)
    sb=Scoreboard(s,screen,stats)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        screen.fill(s.bg_color)
        gf.check_events(s,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(s,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(s,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(s,screen,stats,sb,ship,aliens,bullets,play_button)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()
