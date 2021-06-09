#Maze_Game


**Dependencies**
The dependencies required to run this game are Python 3, Flask, and Pygame

How to Run the Code

1. Create a virtual environment by opening the windows terminal or powershell by running the command “python -m venv vir_env”, or in Unix run the command “python3 -m venv __virtualEnv”
2. After creating the virtual environment, activate it by running “.\__virtualEnv\Sctripts\activate.bat” in windows terminal, or “.\__virtualEnv\Sctripts\activate.ps1” in powershell, or “source _virtualEnv/bin/activate” for unix machines
   1. Upon activating the virtual environment, your command line should change to have “(__virtualEnv)” at the beginning
3. Run the command  “pip install pygame” as well as "pip install Flask" on the command line
4. After pygame finishes installing, run ‘main.py’ by typing “python main.py”

---



**Web API**
To see your highscores stored on a webpage once you have completed a few games:

1. cd into the web folder run app.py by typing "python app.py"
2. Visit the link displayed in the console to see your scores. Enter the link into your browser and add "/api/list" to the end of the URL. For example: localhost:3000/api/list
3. You will now be able to see the highscore along with the player's name who set those scores.

---



**How to Control the Game**
W Key

- Releasing the W key will allow the Player to move one spot up.
- Holding the W key down will allow the Player to continuously move up at a rate of one spot per second.
  A Key
- Releasing the A key will allow the Player to move one spot left
- holding the A key down will allow the Player to continuously move left at a rate of one spot per second.
  S Key
- Releasing the S key will allow the Player to move one spot down
- Holding the S key down will allow the Player to continuously move down at a rate of one spot per second.
  D Key
- Releasing the D key will allow the Player to move one spot right
- Holding the D key down will allow the Player to continuously move right at a rate of one spot per second.
  Q and ESC Key
- Pressing the Q or ESC key will close the pygame window

---



**Win Condition**
To win you first have to collect all the items randomly laid out in the maze and proceed to the exit before time runs out.

**Lose Condition**

* Reach the exit without collecting all the items
* Time reaches 0 before player collects all the items and reaches exit.
