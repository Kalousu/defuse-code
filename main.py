import pygame
from Button import Button

pygame.init()

screen = pygame.display.set_mode()
size = pygame.display.get_window_size()
width = size[0]
height = size[1]
print(width, height)

clock = pygame.time.Clock()

text_font = pygame.font.SysFont("Arial", 50)

def main_menu():

    while True:
        MENU_TEXT = text_font.render("Main Menu", True, "#ffffff")
        MENU_RECT = MENU_TEXT.get_rect(center=((width / 2), 100))

        PLAY_BUTTON = Button(image=pygame.image.load("./assets/Button.png"), pos=((width/2), 250), 
                                text_input="PLAY", font=text_font, base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("./assets/Button.png"), pos=((width/2), 450), 
                                text_input="OPTIONS", font=text_font, base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("./assets/Button.png"), pos=((width/2), 650), 
                                text_input="QUIT", font=text_font, base_color="#d7fcd4", hovering_color="White")    
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        

        # Do logical updates here.
        # ...

        screen.fill("black")  # Fill the display with a solid color
        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        print("HI")
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        print("Hi")
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        raise SystemExit
        

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)

main_menu()