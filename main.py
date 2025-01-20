import pygame

pygame.init()

screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
width = size[0]
height = size[1]
print(width, height)

imp = pygame.image.load("./assets/Bild.jpeg").convert()
imp = pygame.transform.scale(imp, (1440,934))

clock = pygame.time.Clock()

text_font = pygame.font.SysFont("Raleway Bold", 100)

def main_menu():
    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT1 = text_font.render("Defuse", True, "#000000")
    MENU_TEXT2 = text_font.render("Code", True, "#000000")
    MENU_RECT1 = MENU_TEXT1.get_rect(center=(150, 100))
    MENU_RECT2 = MENU_TEXT2.get_rect(center=(115, 180))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        # ...

        

        screen.fill("black")  # Fill the display with a solid color
        screen.blit(imp, (0, 0))
        screen.blit(MENU_TEXT1, MENU_RECT1)
        screen.blit(MENU_TEXT2, MENU_RECT2)

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)

main_menu()