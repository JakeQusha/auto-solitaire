import game_scaner as gf
from solver import solve
from executor import execute
import time
from definitions import Config
if __name__ == "__main__":
    config = Config('config.json')
    print(config)
    res = solve(gf.make_board(config))
    if not res[1]:
        print("no no")
        exit(0)
    print(f"found solution in {len(res[0])} moves")
    execute(res[0],config)


