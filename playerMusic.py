import pygame
from pygame import mixer

pygame.init()
mixer.init()
mixer.music.load ('Naps (ft. Sofiane & Kalif Hardcore) Chicha kaloud (Clip Officiel) (1).mp3')
mixer.music.set_volume(1.4)
mixer.music.play() 

largeur, hauteur = 400, 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Lecteur de musique")

blanc = (255, 255, 255)
noir = (0, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 20)

def afficher_texte(texte, x, y):
    texte_surface = font.render(texte, True, noir)
    texte_rect = texte_surface.get_rect(center=(x, y))
    fenetre.blit(texte_surface, texte_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
            elif event.key == pygame.K_r:
                mixer.music.unpause()
            elif event.key == pygame.K_e:
                mixer.music.stop()
                running = False

    fenetre.fill(blanc)  
    afficher_texte("Pressez 'p' pour mettre en pause", largeur // 2, hauteur // 2 - 20)
    afficher_texte("Pressez 'r' pour reprendre la lecture", largeur // 2, hauteur // 2 + 20)
    afficher_texte("Pressez 'e' pour sortir du programme", largeur // 2, hauteur // 2 + 60)

    pygame.display.flip()

pygame.quit()
