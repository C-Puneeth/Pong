# Pong Game

This is a simple implementation of the classic Pong game using Python and the Turtle graphics library.

## Project Structure

```
Pong/
├── ball.py
├── main.py
├── midline.py
├── paddle.py
├── scoreboard.py
└── __pycache__/
    └── ...
```

## Files

- `ball.py`: Contains the `Ball` class which handles the ball's movement and collision logic.
- `main.py`: The main entry point of the game. It sets up the game screen, initializes game objects, and contains the game loop.
- `midline.py`: Contains the `Mid_Line` class which draws the midline on the game screen.
- `paddle.py`: Contains the `Paddle` class which handles the paddle's movement.
- `scoreboard.py`: Contains the `Scoreboard` class which handles the display and updating of the game score.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the Turtle graphics library if you haven't already:
    ```sh
    pip install PythonTurtle
    ```
3. Run the `main.py` file to start the game:
    ```sh
    python main.py
    ```

## Controls

- Player 1 (left paddle): Use the `W` key to move up and the `S` key to move down.
- Player 2 (right paddle): Use the `Up` arrow key to move up and the `Down` arrow key to move down.

## Game Rules

- The ball bounces off the top and bottom edges of the screen.
- The ball bounces off the paddles when it collides with them.
- If the ball passes the right edge, Player 1 scores a point.
- If the ball passes the left edge, Player 2 scores a point.
- The game continues indefinitely until you close the game window.

## License

This project is licensed under the MIT License.