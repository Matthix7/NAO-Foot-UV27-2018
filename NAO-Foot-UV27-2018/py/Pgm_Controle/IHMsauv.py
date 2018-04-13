#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 10:56:09 2018

@author: matthieu


Affichage graphique sur écran :
    -affichage de la commande exécutée par l'utilisateur (manette)
    -affichage carte du terrain
"""

import pygame
from pygame.locals import* 

def IHM():
    
    pygame.init()
    
    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((709,489), RESIZABLE)
    
    #Chargement et collage du fond
    fond = pygame.image.load("terrain-de-football.jpg").convert()
    fenetre.blit(fond, (0,0))
    
    #Chargement fleche
    arrow = pygame.image.load("fleche.png")
    arrow.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
    
    #Chargement et collage du robot
    perso = pygame.image.load("robot_nao.png").convert_alpha()
    fenetre.blit(perso, (310,150))
    
    #Rafraîchissement de l'écran
    continuer = 1

    #Boucle infinie
    while continuer:
        pygame.display.flip()
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            
            if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #Si "flèche haut"
                    print("toto")
                    fenetre.blit(arrow, (450,110))
                    pygame.display.flip()





IHM()