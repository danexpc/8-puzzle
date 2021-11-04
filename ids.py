from puzzle import Puzzle
from node import Node


def dls(start: Puzzle, goal: Puzzle, depth: int) -> (list[str], int):
    depth_limit: int = depth
    nodes: list[Node] = [Node(start, None, None, 0)]
    count: int = 0
    explored: list[Puzzle] = []

    while nodes:
        node: Node = nodes.pop(0)
        count += 1
        explored.append(node.get_puzzle())

        if node.get_puzzle() == goal:
            return node.path_from_start(), count

        if node.depth < depth_limit:
            for item in node.expand():
                if item.get_puzzle() not in explored:
                    nodes.insert(0, item)


def ids(start: Puzzle, goal: Puzzle, depth: int = 50) -> (list[str], int):
    for i in range(depth):
        result = dls(start, goal, i)
        if result is not None:
            return result
