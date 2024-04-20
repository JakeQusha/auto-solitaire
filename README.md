# Auto Solitaire (WIP)

MOLEK-SYNTEZ solitaire solver written in python.

## SHOWCASE
https://github.com/JakeQusha/auto-solitaire/assets/79422805/e6946b5d-f08b-47c8-9336-25c802664603

## What works
- Capturing screen with game*
- Solving**
- Executing generated solution*

##### *All screens must be same resolution (preferably 1080p)
##### **Generated solutions have about 100-400 moves which is quite a lot

## What needs to be done
- Rework solving process to find best solution instead of first solver stumbles upon.
- add support for setups with different screen resolution configuration.

## Installation and Use
- install pyautogui and pillow.
- in settings.json change your screen amount and set on which one you have the game on.
- lunch molek-syntez, open solitaire and click new game.
- lunch main.py.

## Not all of my monitors are 1080p
#### all of them are the same resolution
  You need to go to settings.json and change ~~magic numbers~~ offsets because the default ones are for 1080p.
#### not all of them are the same resolution
  Just disable or downscale the ones with higher resolution.
