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
    fenetre = pygame.display.set_mode((489,709), RESIZABLE)
    
    #Chargement et collage du fond
    fond = pygame.image.load("terrain-de-football.jpg").convert()
    fenetre.blit(fond, (0,0))
    
    #Chargement fleches
    arrow = pygame.image.load("fleche.png")
    arrow_rot_l = pygame.image.load("fleche_rot_l.png")
    arrow_rot_r = pygame.image.load("fleche_rot_r.png")
    
    #Chargement et collage du robot
    perso = pygame.image.load("robot_nao.png").convert_alpha()
    fenetre.blit(perso, (190,260))
    
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
                if event.key == pygame.K_z: #Si "flèche haut"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_up = pygame.transform.rotate(arrow, 90)
                    fenetre.blit(arrow_up, (110,0))
                    pygame.display.flip()
                    
                if event.key == pygame.K_s: #Si "flèche bas"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_down = pygame.transform.rotate(arrow, -90)
                    fenetre.blit(arrow_down, (110,450))
                    pygame.display.flip()
                    
                if event.key == pygame.K_d: #Si "flèche droite"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_right = pygame.transform.scale(arrow_rot_r, (300, 300))
                    fenetre.blit(arrow_right, (100,220))
                    pygame.display.flip()
                    
                if event.key == pygame.K_q: #Si "flèche gauche"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_left = pygame.transform.scale(arrow_rot_l, (300, 300))
                    fenetre.blit(arrow_left, (100,220))
                    pygame.display.flip()
                    
                if event.key == pygame.K_a: #Si "flèche diag av gauche"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_dbl = pygame.transform.rotate(arrow, 140)
                    arrow_dbl = pygame.transform.scale(arrow_dbl, (150, 300))
                    arrow_dbl.set_colorkey((255,255,255))
                    fenetre.blit(arrow_dbl, (70,70))
                    pygame.display.flip()
                    
                if event.key == pygame.K_e: #Si "flèche diag av droit"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_dbl = pygame.transform.rotate(arrow, 40)
                    arrow_dbl = pygame.transform.scale(arrow_dbl, (150, 300))
                    arrow_dbl.set_colorkey((255,255,255))
                    fenetre.blit(arrow_dbl, (250,70))
                    pygame.display.flip()

                if event.key == pygame.K_w: #Si "flèche diag arr gauche"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_dbl = pygame.transform.rotate(arrow, -140)
                    arrow_dbl = pygame.transform.scale(arrow_dbl, (150, 300))
                    arrow_dbl.set_colorkey((255,255,255))
                    fenetre.blit(arrow_dbl, (70,370))
                    pygame.display.flip()
                
                if event.key == pygame.K_x: #Si "flèche diag arr droit"
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(perso, (190,260))
                    arrow_dbl = pygame.transform.rotate(arrow, -40)
                    arrow_dbl = pygame.transform.scale(arrow_dbl, (150, 300))
                    arrow_dbl.set_colorkey((255,255,255))
                    fenetre.blit(arrow_dbl, (250,370))
                    pygame.display.flip()


IHM()