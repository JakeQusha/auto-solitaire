import game_scaner as gf
from definitions import Config
if __name__ == "__main__":
    config = Config('config.json')
    print(config)
    gf.make_board(config)
