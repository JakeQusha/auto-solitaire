from src import game_scaner as gf
from src.solver import solve
from src.executor import execute
from src.definitions import Config

if __name__ == "__main__":
    config = Config('config.json')
    print(config)
    res = solve(gf.make_board(config))
    if not res[1]:
        print("No Solutions found")
        exit(0)
    print(f"found solution in {len(res[0])} moves")
    execute(res[0], config)
    print("Done!")
