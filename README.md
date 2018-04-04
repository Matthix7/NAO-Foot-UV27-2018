# NAO-Foot-UV27-2018
NAO Soccer Challenge 2018 (UV 2.7)

Base de départ pour la compétition NAO Foot UV 2.7 2017

Pour la mise au point avec le simulateur V-REP, deux scénarios (dans le dossier scenes du répertoire) sont disponibles :  
nao-UV27-2018-one-robot-yellow-ball-save-image.ttt (port 11212)
nao-UV27-2018-two-robots-yellow-ball-save-image.ttt ports 11212 et 11216)

Les fichiers (archives binaires) utiles au projet mais non gérés par git sont :
- pynaoqi-20170505.tgz   pour la commande du robot NAO en python 2.7
- naoqi-20170505.tgz     "intelligence" du robot NAO
- v-rep-20170505.tgz     simulateur dynamique V-REP

Ces archives peuvent être récupérées sur /public/share/uv27spid 

Pour les insèrer ces archives à votre projet, placez vous dans le répertoire principal et decompressez-les avec les commandes suivantes

tar xfz /public/share/uv27spid/pynaoqi-20170505.tgz
tar xfz /public/share/uv27spid/naoqi-20170505.tgz
tar xfz /public/share/uv27spid/v-rep-20170505.tgz