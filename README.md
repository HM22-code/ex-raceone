# ex-raceone

A retro side scroller game made with pygame

## TODO

- [ ] Use base engine to make a template
- [ ] Create a functional prototype
- [X] Plan game architecture and concepts

## Look and feel

- SNES style graphics 16 bit
- 16*9 for widescreen diplays
- HD resolutions must be divisible by the games resolution so scaling works
- Native resolution is 480*270 (this is 1/4 of 1920*1080)

## Guides & Advises

### No Repeats

If code is repeated, make a class or function of it

### Use inheritance

Sprite > Static Entity > Dynamic Entity > Player

### Resolution

We will implement a system where scaling the game is very efficient and doesn't actually increase the native resolution of the game itself, only the display.
We will also go over how to turn on hardware acceleration for if the user chooses to turn fullscreen mode on.

### Layers

- BG 3
- BG 2
- BG 1
- Enemy
- Player
- Projectiles
- UI

### Game controller

- The controller is the core of the entire program
- The program pretty much start with the controller
- The controller contain the main game loop
- The controller contains and execute every game state (menu, level, ending, ...)
- It contains the logic for how to swap these state when necessary and how to clean them up

### State system

- Create a state class that contain all the logic necessary for states (game state, entity state)
- Every dynamic entity will have a stateGroup object that contains all of there states
The entitity can commands to this state group, and the state group will take care of its logic

### Animation system

- Every Dynamic entity will have an animation group similar to the state group
- The group will contain a list of all possible animation cycles and handle animation
- It will contains a function for sprite sheet to cut the sprites to an animation object
- Doing things this way with the animation state objects, removes a ton of code that would have to go into the entity classes themselves and makes it much easier to program once it is all implemented

### Constants file

- This file is like the .ini file found with a ton of games. it contains a ton of static variables that are used all through out your program. Window information, joystick information, game state names, directory information, fps, ...

### Event handler

- The eevent handler object will contain all the code for handling user input
- It will also have a joystick system in it that will work with any type of direct input or xinput device
- It will also be using a command design pattern for encapsulating the button input into their own object
- This will allow to give users an option to reassign buttons in game if they would like

## Brainstorming

- Side scroller game
  - Jeux style du dinosaure en ligne
  - style scrolling permanent
  - style retro arcade 8-bit 16-bit
  - style jetpack joyride

- 2 routes parallèles pour esquiver des obstacles en changeant de route

- Objectifs aller le plus loin possible
  - ou terminer le niveau
  - niveaux prédéfinis/ construit  avec tiles ?
  - éviter les obstacles
  - side scrolling race game

- Environnement et ressources:
  - futuriste,
  - hyper dynamique,
  - retro,
  - cyberpunk

- Style pyxel art + Spritessheet à prévoir

- Music pack de music Retro

- Premier jeux:
  - Moteur de jeux: Pygame
  - Langage de prog: Python

- Menu de sélection
  - Hub avec les différents niveaux
  - représenteé par des planetes animées
  - avec le planete generator

- Idéees
  - voir le déclun de la terre
  - planetes futuriste et post apo cyber
  - lore + commandes expliquer bulle de texte sur fondu

- Crédits

- ++ Bonus:
  - Score
  - Menu Option

- 3 différents niveaux Difficulté croissante

- Esquiver des obstacles

- Tirer des lasers

- Ennemis:
  - police
  - Boss

- Système de vie:
  - Barre de vie
  - Prendre le moins de dégats possible

- Avant de commencer un niveau Sprites:
  - READY
  - GO

- Vaisseau Terrestre

- Possibilité de saut en cloche

- Fin sur credit
  - fond panorama sur les wastelands
  - scrolling vers le ciel
  - etiles fillantes vaisseaux
  - espace nouvelle espoir vers l'infini
  - fin
