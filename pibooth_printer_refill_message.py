import time
import pygame
import pibooth
from pibooth import pictures, fonts


__version__ = "0.1.0"

SECTION = 'PRINTER REFILL MESSAGE'

@pibooth.hookimpl
def pibooth_configure(cfg):
    cfg.add_option(
         SECTION,
         'text_refill',
         "Please refill printer paper and/or cartridge(s).",
         "Text to display when max_pages is reached"
    )
    cfg.add_option(
        SECTION,
        'text_done',
        "Done?",
        "Confirmation button for the refill"
    )
    cfg.add_option(
        SECTION,
        'image_path',
        "assets/refill_instructions.png",
        "Path to the image with the refill instructions"
    )

@pibooth.hookimpl
def state_wait_do(win, app , cfg, events):     

    if app.count.printed >= cfg.getint('PRINTER', 'max_pages') and cfg.getint('PRINTER', 'max_pages') != -1:
        
        win_rect = win.surface.get_rect()

        # Get best font size according to window size
        font = fonts.get_pygame_font(
            cfg.get(SECTION, 'text_refill'),
            fonts.CURRENT, 
            win_rect.width//1.5, 
            win_rect.height//1.5
        )

        # Clear screen
        if isinstance(win.bg_color, (tuple, list)):
            win.surface.fill(win.bg_color)
        else:
            bg_surface = pictures.get_pygame_image(win.bg_color, win_rect.size, crop=True, color=None)
            win.surface.blit(bg_surface, (0, 0))

        # Draw the surface at screen
        text_surface = font.render(cfg.get(SECTION, 'text_refill'), True, win.text_color)
        pos = (win_rect.center[0]- win_rect.width//3, win_rect.top + win_rect.height//4)
        win.surface.blit(text_surface, pos)
        
        # Draw Done button
        text_surface = font.render(cfg.get(SECTION, 'text_done'), True, win.text_color)
        pos = (win_rect.center[0]+ win_rect.width*0.2,win_rect.center[1] + win_rect.height*0.15)
        win.surface.blit(text_surface, pos)
        
        # Draw picture
        size = [win_rect.width//2, win_rect.height//2]
        picture = pictures.get_pygame_image(cfg.get(SECTION, 'image_path'), size, hflip=False, vflip=False, color= win.text_color)
        x = int(win_rect.left)
        y = int(win_rect.bottom - size[1])
        picture_pos = (x,y)
        win.surface.blit(picture, picture_pos)

        # Force screen update and events process
        pygame.display.update()
        pygame.event.pump()
        events = pygame.event.get()
        
        # wait for user confirmation
        if app.find_capture_event(events) != None or app.find_print_event(events) != None:
            # reset printed images counter
            app.count.printed = 0