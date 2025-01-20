import pygame

pygame.init()

screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
width = size[0]
height = size[1]
print(width, height)

clock = pygame.time.Clock()

text_font = pygame.font.SysFont("Arial", 30)

def main_menu():
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = text_font.render("Main Menu", True, "#ffffff")
    MENU_RECT = MENU_TEXT.get_rect(center=((width / 2), 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        # ...

        screen.fill("black")  # Fill the display with a solid color
        screen.blit(MENU_TEXT, MENU_RECT)

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)

main_menu()