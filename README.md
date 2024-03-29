# FlappyBird Knockoff with Pygame

This is a simple FlappyBird knockoff game created using Pygame, a popular Python library for creating 2D games. In this game, you control a bird and try to navigate it through a series of pipes by tapping the spacebar to flap its wings and avoid collisions. 

## Screenshots

<p align="center">
  <img src="Assets/Screenshots/Start.png" alt="Start"/>
</p><p align="center">
  <img src="Assets/Screenshots/Death.png" alt="Death"/>
</p>

## Requirements
- Python 3.x
- Pygame

## Installation
1. Clone or download this repository to your local machine.
2. Grab the latest release of Python from [here](https://www.python.org/downloads/) **and** install Pygame by executing 
```bash 
pip install pygame
```

**Note:** If the ``pip install pygame`` did not work for you, then try this:
1. Windows:
```bash
python -m pip install pygame
```
2. Mac: 
```bash
python3 -m pip install pygame
```
3. Linux:
Same as windows.

## How to Play
- Press the spacebar to make the bird flap its wings and navigate through the pipes.
- Avoid collisions with the pipes.
- Your score increases as you pass through each pair of pipes.
- The game ends if the bird collides with a pipe or if it hits the ground.

## Controls
- **Spacebar:** Flap wings to fly.
- **R:** Reset

## Files
- **main.py:** Main Python script containing the game code.
- **assets:** Directory containing game assets such as images and sounds.

## Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or create a pull request.

## Acknowledgments
This project was inspired by the classic game Flappy Bird developed by Dong Nguyen. Special thanks to the Pygame community for their excellent resources and tutorials.

## License
This project is licensed under the [MIT License](LICENSE.md).