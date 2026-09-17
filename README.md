# AimBot

Ce projet est un AimBot simple qui a pour but de battre des records sur l'Aim Trainer suivant : [3D Aim Trainer](https://app.3daimtrainer.com/play).

C'est un script Python unique qui utilise la bibliothèque `mss` pour la capture d'écran et `cv2` (OpenCV) pour la reconnaissance d'image.

En termes de performances, la vitesse est réglable via la variable `level` (ligne 10). Plus la valeur de `level` est basse, plus le bot est rapide. Il est réglé par défaut sur 2 (la valeur 1 étant trop instable).

Le score maximum obtenu sur le mode *Tile Frenzy* est de **272** (soit environ 9 cibles par seconde). Cependant, les résultats peuvent varier en fonction de l'apparition aléatoire des cibles et du léger bruit de ciblage artificiel implémenté dans le code.

## Démo en vidéo (level = 3)

[Voir la vidéo de démonstration sur Medal.tv]([https://medal.tv/games/screen-capture/clips/nxR1XRovkXgp9NP4g?invite=cr-MSxwSGIsMjA5OTUzODMy])

Le script small.py est quant à lui spécialiste de la précision sur de petites cibles
