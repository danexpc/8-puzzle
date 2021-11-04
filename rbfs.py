from __future__ import annotations

from puzzle import Puzzle
from node import Node
from sys import maxsize

count = 1


def rbfs(start: Puzzle, goal: Puzzle) -> (list[str], int):
    global count

    count = 1

    node, _ = rbfs_search(Node(start, None, None, 0), maxsize, goal)

    return node.path_from_start(), count


def rbfs_search(node: Node, f_limit: int, goal: Puzzle) \
        -> tuple[Node | None, int | None]:
    global count

    successors: list[tuple[int, Node]] = []

    if node.get_puzzle() == goal:
        return node, None

    children: list[Node] = node.expand()

    if not len(children):
        return None, maxsize

    for child in children:
        count = count + 1
        successors.append((child.puzzle.h2(), child))
    while len(successors):
        successors.sort(key=lambda x: x[0])
        best_node: Node = successors[0][1]
        if best_node.puzzle.h2() > f_limit:
            return None, best_node.puzzle.h2()
        alternative_value: int = successors[1][0]

        result_node, result_value = rbfs_search(
            best_node, min(f_limit, alternative_value), goal
        )

        successors[0] = (result_value, best_node)

        if result_node is not None:
            break
    return result_node, None
