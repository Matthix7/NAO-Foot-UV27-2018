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

def init():
    pygame.init()
    fenetre = pygame.display.set_mode((640, 480))
    aff = int(input())
    while aff:
        continue
        aff = int(input())