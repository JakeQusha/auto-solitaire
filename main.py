import game_former as gf
from config import Config
if __name__ == "__main__":
    config = Config('config.json')
    print(config)
    gf.make_board(config)
