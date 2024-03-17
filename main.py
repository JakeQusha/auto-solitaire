import game_scaner as gf
from solver import solve
from definitions import Config
if __name__ == "__main__":
    config = Config('config.json')
    print(config)
    solve(gf.make_board(config))
