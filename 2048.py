# 2048 game python code
# Import module
import turtle
import random


class game:
    """Game class with inherit from Turtle frame widget."""

    def __init__(self):
        """This is the constructor on self"""
        self.screen = turtle.Screen()
        self.screen.setup(800, 700)  # Setup screen size
        self.screen.bgcolor("#faf8ef")  # Setup background color
        self.screen.title("2048 game")  # Title Name
        self.screen.tracer(0)  #

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(-400, 400)  # Ready to draw board
        self.pen.pendown()
        self.pen.pensize(3)  # Set pen size
        self.pen.speed(0)

        self.position = -240, 240
        self.cell_size = 120
        self.size = 4
        self.score = 0
        self.board = [[0 for i in range(4)] for j in range(4)]  # Empty board
        self.cells = []
        self.last_key = ''

        self.board_maker()
        self.start_game()

        self.screen.listen()
        self.screen.onkey(self.left, 'Left')  # Calling left arrow function
        self.screen.onkey(self.right, 'Right')  # Calling right arrow function
        self.screen.onkey(self.up, 'Up')  # Calling up arrow function
        self.screen.onkey(self.down, 'Down')  # Calling down arrow function
        self.screen.onkey(self.game_quit, 'Escape')  # Calling Esc key function
        self.screen.onkey(self.restart, 'n')  # Calling n key function
        self.screen.onkey(self.invalid_key, '')  # Calling any other keys
        self.screen.update()

        turtle.done()

    # Set cell color palette
    cell_colors = {
        0: '#ccc1b4',
        2: '#EDE3DA',
        4: '#EEE0C9',
        8: '#F2B279',
        16: '#F69563',
        32: '#F67C5F',
        64: '#F65F3B',
        128: '#EDD073',
        256: '#EDCC61',
        512: '#EDC850',
        1024: '#edc53f',
        2048: '#edc22e'
    }
    # Set number color palette
    number_colors = {
        0: '#ccc1b4',
        2: "#766D65",
        4: "#766D65",
        8: "#ffffff",
        16: "#ffffff",
        32: "#ffffff",
        64: "#ffffff",
        128: "#ffffff",
        256: "#ffffff",
        512: "#ffffff",
        1024: "#ffffff",
        2048: "#ffffff"
    }

    def board_maker(self):
        """Create a function to make a board"""
        # Set up basic screen
        self.pen.penup()
        self.pen.goto(0, -300)
        self.pen.color('#766D65')
        # Directions for how to do exit and re-rerun
        self.pen.write("Press 'Esc' to quit or 'n' to restart.", move=False,
                       align='center', font=('Arial', 25, 'bold'))
        self.pen.goto(-245, 250)
        # Directions for arrow keys
        self.pen.write("Last key: " + str(self.last_key), move=False,
                       align='left',
                       font=('Arial', 30, 'bold'))
        self.pen.color('#BBAC9F')
        self.pen.goto(180, 250)
        # Directions for score board
        self.pen.write("Score: " + str(self.score), align="center",
                       font=("Arial", 30, "bold"))
        self.pen.pensize(15)
        # Set up the spot which is starting to draw
        x, y = -240, 240
        # Draw grid with guid line
        for i in range(self.size):
            for j in range(self.size):
                self.pen.penup()
                self.pen.goto(x + j * 120, y - i * 120)
                self.pen.pendown()
                self.pen.fillcolor(game.cell_colors[self.board[i][j]])
                self.pen.begin_fill()
                for k in range(4):
                    self.pen.forward(self.cell_size)
                    self.pen.right(90)
                self.pen.end_fill()
        self.screen.update()

    def start_game(self):
        """Create a function to start 2048 game"""
        # Set up a board filled with 0
        self.board = [[0 for i in range(4)] for j in range(4)]
        # Define each spot to (i, j)
        empty_cells = [(i, j) for i in range(self.size) for j in range(
            self.size) if
                       self.board[i][j] == 0]
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        # Convert to two empty cells to '2'cell
        if empty_cells:
            self.board[row][col] = 2
            self.board_maker()
        while self.board[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.board[row][col] = 2
        self.board_maker()
        self.draw_number()

    def draw_number(self):
        """Create a function to draw number on board"""
        # Target each cell and position (i, j) and (x, y)
        for i in range(self.size):
            for j in range(self.size):
                x, y = self.position[0] + j * self.cell_size + self.cell_size \
                       // 2, \
                       self.position[
                           1] - i * self.cell_size - self.cell_size + 30
                if self.board[i][j] == 0:
                    number = ''
                else:
                    number = self.board[i][j]
                self.pen.penup()
                self.pen.goto(x, y)
                self.pen.color(game.number_colors[self.board[i][j]])
                self.pen.write(number, move=False, align='center',
                               font=('Arial', 48, 'bold'))

    def stack(self):
        """Compress all non-zero number in empty board"""
        matrix = [[0] * 4 for _ in range(4)]
        # The value in the cell is non-zero, fill position to the value
        for i in range(4):
            position_fill = 0
            for j in range(4):
                if self.board[i][j] != 0:
                    matrix[i][position_fill] = self.board[i][j]
                    position_fill += 1
        self.board = matrix

    def combine(self):
        """Add together all horizontally adjacent non-zero numbers"""
        for i in range(4):
            for j in range(3):
                # Multiply the value (i, j) by 2 and (i, j+1) is converted 0
                if self.board[i][j] != 0 and self.board[i][j] == \
                        self.board[i][j + 1]:
                    self.board[i][j] *= 2
                    self.board[i][j + 1] = 0
                    self.score += self.board[i][j]

    def reverse(self):
        """Reverse the order of each row on the board"""
        matrix = []
        # Value gets reversed after nested for loop set on matrix
        for i in range(4):
            matrix.append([])
            for j in range(4):
                matrix[i].append(self.board[i][3 - j])
        self.board = matrix

    def transpose(self):
        """Flip the board over its diagonal"""
        matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                # Set.matrix equal to updated board
                matrix[i][j] = self.board[j][i]
        self.board = matrix

    def add_tile(self):
        """Add new tiles randomly to an empty cell"""
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while self.board[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        # Add random number 2 or 4(I set the chance to occur 4 is 1%)
        self.board[row][col] = 2 if random.random() < 0.99 else 4

    def update_board(self):
        """Create a function to update board"""
        for i in range(4):
            for j in range(4):
                # Check cells have a zero value and display cell with no text
                x, y = self.position[0] + j * self.cell_size + self.cell_size \
                       // 2, \
                       self.position[
                           1] - i * self.cell_size - self.cell_size + 30
                cell_value = self.board[i][j]
                # If a cell value is 0
                if cell_value == 0:
                    self.pen.penup()
                    self.pen.goto(x, y)
                # If a cell value is non-zero
                else:
                    self.pen.penup()
                    self.pen.goto(x, y)
        self.board_maker()
        self.draw_number()
        self.screen.update()

    def left(self):
        """Left movement function(logic)"""
        matrix_check = self.board
        self.last_key = 'left'
        self.pen.clear()
        self.stack()
        self.combine()
        self.stack()
        if matrix_check != self.board:
            self.add_tile()
        self.board_maker()
        self.update_board()
        self.game_over()

    def right(self):
        """right movement function(logic)"""
        matrix_check = self.board
        self.last_key = 'right'
        self.pen.clear()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        if matrix_check != self.board:
            self.add_tile()
        self.update_board()
        self.game_over()

    def up(self):
        """Up movement function(logic)"""
        matrix_check = self.board
        self.last_key = 'up'
        self.pen.clear()
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        if matrix_check != self.board:
            self.add_tile()
        self.update_board()
        self.game_over()

    def down(self):
        """Down movement function(logic)"""
        matrix_check = self.board
        self.last_key = 'down'
        self.pen.clear()
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        if matrix_check != self.board:
            self.add_tile()
        self.update_board()
        self.game_over()

    def invalid_key(self):
        """Display message if any key other is pressed"""
        self.pen.goto(0, 0)
        self.pen.color('#766D65')
        self.pen.write("Do something if any key is pressed",
                       align="center", font=("Arial", 27, "bold"))

    def game_quit(self):
        """Function to quit game"""
        turtle.bye()

    def restart(self):
        """Function to restart game"""
        self.pen.clear()
        self.score = 0
        self.board_maker()
        self.start_game()

    def Exists_horizontalMoves(self):
        """Check any possible of horizontal move"""
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j + 1]:
                    return True
        return False

    def Exists_verticalMoves(self):
        """Check any possible of vertical move"""
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i + 1][j]:
                    return True
        return False

    def game_over(self):
        """Check game win or lose"""
        if any(2048 in row for row in self.board):
            self.pen.penup()
            self.pen.goto(0, 0)
            self.pen.color('#766D65')
            self.pen.write("YOU WIN!!. Press 'Esc' to quit or 'n' to restart.",
                           align="center",
                           font=("Arial", 25, "bold"))
            self.screen.update()
        elif not any(0 in row for row in
                     self.board) and not self.Exists_horizontalMoves() and not \
                self.Exists_verticalMoves():
            self.pen.penup()
            self.pen.goto(0, 0)
            self.pen.color('#766D65')
            self.pen.write(
                "game OVER!!. Press 'Esc' to quit or 'n' to restart.",
                align="center",
                font=("Arial", 25, "bold"))
            self.screen.update()


def main():
    game()


if __name__ == "__main__":
    main()
