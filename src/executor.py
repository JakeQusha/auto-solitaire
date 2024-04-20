import pyautogui as p
from src.definitions import Config

MAGIC_NUMBER = 10


def get_loc(config: Config, stosik_size: list, loc: (int, int, int)) -> (int, int, int, int):
    width, height = p.size()
    corner = config.get_corrected_offsets(width, height)[0:2]
    return corner[0] + MAGIC_NUMBER + loc[0] * 164, corner[1] + MAGIC_NUMBER + (stosik_size[loc[0]] - loc[1]) * 32, \
           corner[0] + MAGIC_NUMBER + loc[2] * 164, corner[1] + MAGIC_NUMBER + stosik_size[loc[2]] * 32


def execute(moves: list[(int, int, int, bool)], config: Config):
    stosik_size = [5] * 6
    p.moveTo(config.get_corrected_offsets(*p.size())[0:2])
    p.click(duration=0.2)
    p.click(duration=0.2)
    for move in moves:
        cmove = get_loc(config, stosik_size, move[0:3])
        stosik_size[move[0]] -= move[1] + 1
        stosik_size[move[2]] += move[1] + 1
        p.moveTo(cmove[0:2])
        p.dragTo(duration=.2)
        p.moveTo(cmove[2:])
        p.dragTo(duration=.2)


if __name__ == "__main__":
    config = Config('../config.json')
    moves = [(4, 0, 0, False), (1, 2, 4, False), (4, 2, 3, False), (3, 0, 5, False), (5, 0, 1, False), (3, 1, 4, False),
             (1, 0, 5, False), (0, 1, 2, False)]
    execute(moves, config)
