import game_scaner as gf
from solver import solve
import time
from definitions import Config
if __name__ == "__main__":
    config = Config('config.json')
    time.sleep(3)
    print(config)
    gf.make_board(config)
    #solve(gf.make_board(config))
