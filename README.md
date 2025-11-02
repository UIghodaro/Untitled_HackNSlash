# Untitled_HackNSlash
Videogame project started and worked on during a vacation to Nigeria.\
A short game to be about raiding a fortress as a mercenary - **the only one sent on said mission for unknown reasons**. There are ideas about the fighting/weapon system, movement system and character system in head. Plans to come back to the project persist.

**Requires:** *Python 3.8+*\
You can check python version by running ``python3 --version`` on macOS/Linux and ``python --version`` on Windows powershell/cmd

## Setup (from repo root)
Using a virtual environment to run the repo for a demo. *If you wish to install dependencies locally, ignore the first 2 lines as they start the virtual environment*:
### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 game.py
```
### Windows PowerShell
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python game.py
```
### Windows Command Prompt
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python game.py                     # Or `python3 game.py` on some systems
```
*Alternatively, to ``python game.py``, you can use ``python editor.py`` to open the level editor*\
If you created a virtual environment, type this into the terminal when done with the demo:
```bash
deactivate  # Shut down the virtual environment
```
*Note: `requirements.txt` has minimal packages. Exact versions will be updated with `pip freeze` once I can access the original dev environment*
## What's included
The game is a 2D platformer with a level editor included. The playable character is given infinite flight as the "Aston University Goose".
- ``game.py`` - Playable demo
- ``editor.py`` - Level editor
- ``gameRss/images/`` - Assets (sprites & tiles)
- ``backEnd/`` - Back-end functionalities including entity, map generation/interaction and general utility code
- ``map.json`` - A ready-made example level

### In-Game Controls
- **Movement**: ``W/A/S/D``
- **Jump**: ``Space``
- **Dash/Run**: ``Shift``

### Editor-Specific Controls
- **Place/Remove block**: ``Left Click - Place | Right Click - Remove``   (Hold to place or remove multiple)
- **Change Block Type/Kind**: ``Scroll Wheel - Change Type | Shift+Scroll Wheel - Change Kind``
- **Misc**: Press ``G`` to toggle on-grid and off-grid placement, then ``O`` to save and overwrite map.json

## Contact
Built by Uyi Ighodaro - www.linkedin.com/in/uyi-ighodaro14572\

