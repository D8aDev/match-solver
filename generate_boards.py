import random
import json

def generate_board(colors, copies_each):
    """Generate one valid board (list of colors)."""
    tiles = []
    for c in colors:
        tiles.extend([c] * copies_each)
    random.shuffle(tiles)
    return tiles

def generate_boards(colors, copies_each, num_boards):
    """Generate many valid boards."""
    boards = []
    for _ in range(num_boards):
        boards.append(generate_board(colors, copies_each))
    return boards

if __name__ == "__main__":
    # Define your game setup
    colors = ["Blue", "Green", "Red", "Purple", "Yellow", "Orange", "Black"]
    copies_each = 3   # each color appears 3 times
    num_boards = 50000  # number of boards to generate

    boards = generate_boards(colors, copies_each, num_boards)

    # Save as JSON (compressed string format to save space)
    with open("boards.json", "w") as f:
        json.dump(boards, f)

    print(f"Generated {len(boards)} boards and saved to boards.json")
