import copy
import sys
import time

from rbfs import rbfs
from ids import ids
from puzzle import Puzzle

sys.setrecursionlimit(2000)


def statistics(func, start_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    start_time = time.time()

    result, count = func(Puzzle(start_state), Puzzle(goal_state))

    end_time = time.time()

    return {
        "time_usage": end_time - start_time,
        "node_usage": count,
        "moves": len(result),
        "path": result
    }


def test(n):
    results = []

    for i in range(n):
        puzzle = Puzzle.get_default_puzzle()
        state = puzzle.shuffle().state
        state_1 = copy.deepcopy(state)
        state_2 = copy.deepcopy(state)

        statistics_1 = statistics(ids, state_1)
        statistics_2 = statistics(rbfs, state_2)
        statistics_1["start_state"] = state
        statistics_2["start_state"] = state

        d = {}
        for k in statistics_1.keys():
            d[k] = tuple(d[k] for d in [statistics_1, statistics_2])

        results.append(d)

    print(
        "{:>4} | {:>40} | {:>4} | {:>25} | {:>5} | {:>6} | {:100}"
            .format("№", "start state", "alg", "time", "nodes", "moves",
                    "path")
    )
    for i in range(n):
        v = results[i]
        print("-" * 150)
        print("{:>4} | {:>40} | {:>4} | {:>25} | {:>5} | {:>6} | {:100}"
              .format(i, ", ".join(map(str, v["start_state"][0])), "IDS",
                      v["time_usage"][0],
                      v["node_usage"][0], v["moves"][0],
                      ", ".join(map(str, v["path"][0]))))
        print("{:>4} | {:>40} | {:>4} | {:>25} | {:>5} | {:>6} | {:100}"
              .format("", "", "RBFS", v["time_usage"][1],
                      v["node_usage"][1], v["moves"][1],
                      ", ".join(map(str, v["path"][1]))))


def main() -> None:
    test(20)


if __name__ == "__main__":
    main()
