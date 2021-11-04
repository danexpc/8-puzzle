from __future__ import annotations
from puzzle import Puzzle


class Node:
    def __init__(self, puzzle: Puzzle, parent: Node | None, operator: str | None, depth: int) -> None:
        self.puzzle: Puzzle = puzzle
        self.parent: Node = parent
        self.operator = operator
        self.depth: int = depth

    def get_puzzle(self) -> Puzzle:
        return self.puzzle

    def get_parent(self) -> Node:
        return self.parent

    def get_moves(self) -> str:
        return self.operator

    def f(self) -> int:
        return self.depth + self.puzzle.h2()

    def path_from_start(self) -> list[str]:
        state_list: list[Puzzle] = []
        moves_list: list[str] = []
        curr_node: Node = self

        while curr_node.get_moves() is not None:
            state_list.append(curr_node.get_puzzle())
            moves_list.append(curr_node.get_moves())
            curr_node = curr_node.parent

        moves_list.reverse()
        state_list.reverse()

        return moves_list

    def expand(self):
        expanded_nodes = [
            Node(self.puzzle.move_up(), self, "up", self.depth + 1),
            Node(self.puzzle.move_down(), self, "down", self.depth + 1),
            Node(self.puzzle.move_left(), self, "left", self.depth + 1),
            Node(self.puzzle.move_right(), self, "right", self.depth + 1)
        ]
        return [node for node in expanded_nodes if node.puzzle is not None]
