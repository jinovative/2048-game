2048 Game README
High-Level Design

The code creates a game of 2048 using Turtle graphics in Python(3.11). It defines a game class that inherits from the Turtle frame widget and includes functions for drawing the board, starting the game, updating the score and cells, and handling player input for moving cells. The board is represented as a 2D list, with each cell holding a value that is a power of 2. The game is won by reaching a cell with a value of 2048.

How to Run

To run the game, simply install the code in a Python environment with the Turtle module. The game can be played by using the arrow keys to move cells in the up, down, left, or right directions. Pressing the "n" key restarts the game, and pressing the "Escape" key quits the game. If any other keys are pressed, the game is not shut down but shows a message to press the proper key.

Features

The program includes the following features:

Draws the game board with Turtle graphics
Allows the player to move cells up, down, left, or right
Updates the score and cells when moves are made
Randomly generates new cells with values of 2 or 4 when cells are moved
Ends the game and displays a message when the player wins or loses
Allows the player to restart or quit the game using the "n" and "Escape" keys, respectively.
