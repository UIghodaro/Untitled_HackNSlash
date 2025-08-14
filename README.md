# Personal Project: Untitled_HackNSlash
Videogame project started and worked on during a vacation to Nigeria. Framework drawn from other project "One Skater Smashed" with a concept changed and a some things expanded upon.
Due to this, the Setup and possible Setup Issues remain the same across READMEs.

## Tech & setup
The game was built such that running game.py from the root should run the entire game.
- If python or pygame is not installed, run the following in bash for dependencies
```bash
pip install python
pip install pygame
```

Following this:
1. run game.py in an IDE or by typing ``python game.py`` in terminal of the repo root to access the game (controls are A and D for left and right movement respectively, spacebar to fly) OR 
2. run editor.py in an IDE or by typing ``python editor.py`` in terminal of the repo root to access the level editor and place your own blocks, changing the map.json file dynamically

### Possible issue
If, when attempting to run game.py or editor.py, an error comes up along the lines of ``The system cannot find specified path: 'gameRss/images/...'`` then it is highly likely the python file is not being run from the root or the folders are not in the root. 
Ensure all folders are in the root, alongside game.py, editor.py and map.json

## Game Scope
The game is an unfinished 2D platformer with a level editor included. The playable character has infinite jumps because why not.

### In-Game Controls
Character is **moved** via **WASD** keys, **spacebar** for **jump** and **shift** while moving in a direction to **DASH** and start **RUNNING**

### In-Editor Controls
Screen/camera is **moved** via **WASD** keys, **left-click** to **place a block** and *hold left-click* to place multiple. **right-click** to **delete a block** and *hold right-click* to delete multiple.

Hold **shift** *and use the* **scroll wheel** to **Switch which block is being placed**.

Press **'G'** *on the keyboard* to **toggle grid mode**. 

Press **'O'** *on the keyboard* to **save the map** to map.json. Extra map features to be added I guess

### Game('s) Vision
The vision was for the game was a short game about raiding a fortress as a mercenary - **the only one sent on said mission for unknown reasons**.
There are ideas about the fighting/weapon system, movement system and character system in head. Plans to come back to the project persist.

Watchers and cloners are encouraged to rip anything and everything from this and improve on it! Game creation is fun!
