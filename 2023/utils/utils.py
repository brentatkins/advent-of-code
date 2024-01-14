from typing import Iterator, Tuple, TypeVar

Location = TypeVar('Location')

GridLocation = Tuple[int, int]

class SquareGrid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def in_bounds(self, id: GridLocation) -> bool:
        x, y = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def neighbours(self, id: GridLocation) -> Iterator[GridLocation]:
        x, y = id
        neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if (x + y) % 2 == 0: neighbours.reverse()
        results = filter(self.in_bounds, neighbours)
        return results
