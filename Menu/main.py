import pygame
import przycisk

pygame.init()

#wielkość okna
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gra")

game_paused = True
status_menu = "menu"
status_car = 1

font = pygame.font.SysFont("arialblack", 40)    #czcionka

TEXT_COL = (255, 255, 255)  #kolor

#ładuje zdjęcia
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
pojazdy_img = pygame.image.load('images/Pojazdy.png').convert_alpha()
strzalka_l_img = pygame.image.load('images/strzalka_l.png').convert_alpha()
strzalka_p_img = pygame.image.load('images/strzalka_p.png').convert_alpha()

car1_img = pygame.image.load('images/car/car1.png').convert_alpha()
car2_img = pygame.image.load('images/car/car2.png').convert_alpha()
car3_img = pygame.image.load('images/car/car3.png').convert_alpha()
car4_img = pygame.image.load('images/car/car4.png').convert_alpha()

#tworzy przycisk
graj_przy = przycisk.Przycisk(710, 100, resume_img, 1)
ustawienia_przy = przycisk.Przycisk(760, 320, options_img, 1)
wyjscie_przy = przycisk.Przycisk(810, 660, quit_img, 1)
grafika_przy = przycisk.Przycisk(226, 75, video_img, 1)
dzwienk_przy = przycisk.Przycisk(225,200, audio_img, 1)
klawisze_przy = przycisk.Przycisk(246,325, keys_img, 1)
powrot_przy = przycisk.Przycisk(810,660, back_img, 1)
pojazdy_przy = przycisk.Przycisk(760, 490, pojazdy_img, 1)
strz_l_przy = przycisk.Przycisk(1700, 500,strzalka_l_img, 1)
strz_p_przy = przycisk.Przycisk(100, 500,strzalka_p_img, 1)

car1_przy = przycisk.Przycisk(730, 100,car1_img, 0.8)
car2_przy = przycisk.Przycisk(730, 100,car2_img, 0.8)
car3_przy = przycisk.Przycisk(730, 100,car3_img, 0.8)
car4_przy = przycisk.Przycisk(730, 100,car4_img, 0.8)

def rysuj_tekst(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#pentla gry
run = True
while run:

  screen.fill((52, 78, 91))

  #gra sprawdza czy jest włączony tryb gry
  if game_paused == True:
    #sprawdza status menu
    if status_menu == "menu":
      #rysuje przyciski
      if graj_przy.rysuj(screen):
        pygame.time.wait(200)
        game_paused = False
      if ustawienia_przy.rysuj(screen):
        pygame.time.wait(200)
        status_menu = "ustawienia"
      if wyjscie_przy.rysuj(screen):
        run = False
      if pojazdy_przy.rysuj(screen):
        pygame.time.wait(200)
        status_menu = "pojazdy"
    #sprawdza czy są włączone ustawienia
    if status_menu == "ustawienia":
      #rysuje przyciski ustawień
      if grafika_przy.rysuj(screen):
        pygame.time.wait(200)
        print("Video Settings")
      if dzwienk_przy.rysuj(screen):
        pygame.time.wait(200)
        print("Audio Settings")
      if klawisze_przy.rysuj(screen):
        pygame.time.wait(200)
        print("Change Key Bindings")
      if powrot_przy.rysuj(screen):
        pygame.time.wait(200)
        status_menu = "menu"
    if status_menu == "pojazdy":
      
      if status_car == 1:
        if strz_l_przy.rysuj(screen):
          status_car = 4
          pygame.time.wait(200)
        if strz_p_przy.rysuj(screen):
          status_car = 2
          pygame.time.wait(200)
        if powrot_przy.rysuj(screen):
          pygame.time.wait(200)
          status_menu = "menu"
        if car1_przy.rysuj(screen):
          pygame.time.wait(200)
          
      if status_car == 2:
        if strz_l_przy.rysuj(screen):
          status_car = 1
          pygame.time.wait(200)
        if strz_p_przy.rysuj(screen):
          status_car = 3
          pygame.time.wait(200)
        if powrot_przy.rysuj(screen):
          pygame.time.wait(200)
          status_menu = "menu"
        if car2_przy.rysuj(screen):
          pygame.time.wait(200)

      if status_car == 3:
        if strz_l_przy.rysuj(screen):
          status_car = 2
          pygame.time.wait(200)
        if strz_p_przy.rysuj(screen):
          status_car = 4
          pygame.time.wait(200)
        if powrot_przy.rysuj(screen):
          pygame.time.wait(200)
          status_menu = "menu"
        if car3_przy.rysuj(screen):
          pygame.time.wait(200)

      if status_car == 4:
        if strz_l_przy.rysuj(screen):
          status_car = 3
          pygame.time.wait(200)
        if strz_p_przy.rysuj(screen):
          status_car = 1
          pygame.time.wait(200)
        if powrot_przy.rysuj(screen):
          pygame.time.wait(200)
          status_menu = "menu"
        if car4_przy.rysuj(screen):
          pygame.time.wait(200)
        
  else:
    rysuj_tekst("Autko robi brum", font, TEXT_COL, 160, 250)
    if status_car == 1:
      car1_przy.rysuj(screen)
    if status_car == 2:
      car2_przy.rysuj(screen)
    if status_car == 3:
      car3_przy.rysuj(screen)
    if status_car == 4:
      car4_przy.rysuj(screen)
    
  #sprawdzanie klawiszy
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()
