from __future__ import annotations
import random


class Puzzle:
    @staticmethod
    def get_default_puzzle() -> Puzzle:
        state: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return Puzzle(state)

    def __init__(self, state) -> None:
        self.state: list[list[int]] = state
        self.width: int = 3

    def __eq__(self, other) -> bool:
        if isinstance(other, Puzzle):
            return self.state == other.state
        else:
            return False

    def display_board(self) -> None:
        print("-------------")
        for arr in self.state:
            print("| %i | %i | %i |" % (arr[0], arr[1], arr[2]))
            print("------------")
        print()

    def move_up(self) -> Puzzle | None:
        return self._make_move(-1, 0)

    def move_down(self) -> Puzzle | None:
        return self._make_move(1, 0)

    def move_left(self) -> Puzzle | None:
        return self._make_move(0, -1)

    def move_right(self) -> Puzzle | None:
        return self._make_move(0, 1)

    def _find_empty_square(self) -> tuple[int, int]:
        for i, x in enumerate(self.state):
            if 0 in x:
                return i, x.index(0)

    def _make_move(self, to_x: int, to_y: int) -> Puzzle | None:
        x, y = self._find_empty_square()

        if (x + to_x) not in [0, 1, 2] or (y + to_y) not in [0, 1, 2]:
            return None

        new_state: list[list[int]] = [row[:] for row in self.state]
        new_state[x][y], new_state[x + to_x][y + to_y] = new_state[x + to_x][y + to_y], new_state[x][y]
        return Puzzle(new_state)

    def h2(self) -> int:
        distance: int = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    x, y = divmod(self.state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    @property
    def actions(self):
        return [self.move_up, self.move_down, self.move_left, self.move_right]

    def shuffle(self):
        puzzle = self
        for _ in range(15):
            tmp = random.choice(puzzle.actions)()
            if tmp:
                puzzle = tmp
        return puzzle
