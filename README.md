**Help MacGyver to escape!**

***Welcome to the wonderful maze of Macgyver.
He will have to find the three different elements and thus...
Defeat the guardian and get out of this infernal labyrinthe.***

==============================================================================================

**Using the game:**

  - Create a virtual environment:
    - linux, mac: virtualenv -p python3 env
    - windows(powershell): virtualenv -p $env:python3 env
  - Activate a virtual environment:
    - linux, mac: source env/bin/activate
    - windows(powershell): ./env/scripts/activate.ps1
  - clone the project with https://github.com/mehdi-monfort/project3.git
  - Install dependencies: pip install -r requirements.txt
  - open the main file: macgyver.py

==============================================================================================

**How to play:**

  - Use the directional arrows on the keyboard for deplace MacGyver.
  - Collect the 3 elements to be able to face the guardian.
  - If you do not have all the objects, you die and the game is restarted.
  - When you win, the game ends.
  - To exit, use the escape key.

==============================================================================================

**To change the level:**

   - Open the laby.txt file
   - edit the maze using:
     - "S" is Start, MacGyver
     - "A" is Arrival, the guardian
     - "+" is a wall
     - " " is a path

  ***Warning: the last line represents the hud (not the modified).***
  
==============================================================================================
