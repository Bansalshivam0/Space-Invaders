Space Invaders Game
A classic Space Invaders arcade game clone built with Pygame, where you control a spaceship to defend against alien invaders.

Description
This is a simple implementation of the classic Space Invaders arcade game. Control your spaceship at the bottom of the screen and shoot down alien invaders before they reach you. The game keeps track of your current score and high score.
Features

Player-controlled spaceship
Multiple enemy UFOs
Score tracking
High score system
Game over detection
Simple collision physics

Installation

Make sure you have Python installed on your system
Install Pygame:

pip install pygame

Clone this repository or download the source code

Required Files
For the game to run properly, you need the following files in your project directory:

main.py - The main game code
background.jpg - Background image for the game
game.png - Game icon for the window
space-invaders.png - Player spaceship image
ufo.png - Enemy UFO image
bullet.png - Bullet image

How to Play

Run the game:

python main.py

Use the left and right arrow keys to move your spaceship
Press the space bar to shoot bullets
Destroy all the enemy UFOs to earn points
Avoid colliding with enemy UFOs
Game ends when an enemy collides with your spaceship

Controls

Left Arrow: Move spaceship left
Right Arrow: Move spaceship right
Space Bar: Fire bullets

Game Mechanics

Enemies move horizontally and drop down when they reach the edge of the screen
When a bullet hits an enemy, the enemy respawns at a random position at the top
Your score increases each time you hit an enemy
The game tracks your highest score achieved
The game ends when an enemy collides with your spaceship

Future Enhancements

Multiple levels with increasing difficulty
Power-ups and special weapons
Sound effects and music
Different enemy types
Lives system

Credits
This game was created using Pygame, a set of Python modules designed for writing video games.
License
This project is open source and available under the MIT License.
