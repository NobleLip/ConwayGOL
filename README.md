
```
 ▄████▄  ▒█████  ███▄    █ █     █░▄▄▄    ▓██   ██▓ ▄████ ▒█████  ██▓    
▒██▀ ▀█ ▒██▒  ██▒██ ▀█   █▓█░ █ ░█▒████▄   ▒██  ██▒██▒ ▀█▒██▒  ██▓██▒    
▒▓█    ▄▒██░  ██▓██  ▀█ ██▒█░ █ ░█▒██  ▀█▄  ▒██ ██▒██░▄▄▄▒██░  ██▒██░    
▒▓▓▄ ▄██▒██   ██▓██▒  ▐▌██░█░ █ ░█░██▄▄▄▄██ ░ ▐██▓░▓█  ██▒██   ██▒██░    
▒ ▓███▀ ░ ████▓▒▒██░   ▓██░░██▒██▓ ▓█   ▓██▒░ ██▒▓░▒▓███▀░ ████▓▒░██████▒
░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ▒ ▒░ ▓░▒ ▒  ▒▒   ▓▒█░ ██▒▒▒ ░▒   ▒░ ▒░▒░▒░░ ▒░▓  ░
  ░  ▒    ░ ▒ ▒░░ ░░   ░ ▒░ ▒ ░ ░   ▒   ▒▒ ▓██ ░▒░  ░   ░  ░ ▒ ▒░░ ░ ▒  ░
░       ░ ░ ░ ▒    ░   ░ ░  ░   ░   ░   ▒  ▒ ▒ ░░ ░ ░   ░░ ░ ░ ▒   ░ ░   
░ ░         ░ ░          ░    ░         ░  ░ ░          ░    ░ ░     ░  ░
░                                          ░ ░                           
```


# Conway's Game of Life (Pygame Implementation)

This is a simple Python script that implements [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) using the Pygame library. The script was created as a learning exercise to explore Python, Pygame, and basic simulation logic.

## Features

- Randomly initialized grid of cells (alive or dead)
- Visualizes the evolution of the Game of Life in real time
- Adjustable grid/block size by changing the `block` variable
- Runs at a smooth frame rate using Pygame

## How It Works

- Each cell in the grid is either alive (white) or dead (black).
- The state of each cell in the next generation is determined by its eight neighbors, following the classic Game of Life rules:
  - Any live cell with two or three live neighbors survives.
  - Any dead cell with exactly three live neighbors becomes a live cell.
  - All other live cells die in the next generation; all other dead cells stay dead.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) (`pip install pygame`)

## How to Run

1. Install Python and Pygame if you haven't already:
   ```sh
   pip install pygame
   ```
2. Run the script:
   ```sh
   python Conway.py
   ```
3. A window will open showing the Game of Life simulation.

## Customization

- **Grid Size:** Change the `Width`, `Height`, or `block` variables at the top of the script to adjust the grid size or cell size.
- **Initial State:** The grid is randomly initialized, but you can modify the initialization logic to set custom patterns.

## Notes

- Close the window to exit the simulation.
- This script is intended for educational purposes and as a starting point for further experimentation.

---

**Author:** NobleLip
