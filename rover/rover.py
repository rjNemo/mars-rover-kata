from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int
    left: str
    right: str


@dataclass
class Rover:
    x: int
    y: int
    direction: str
    obstacles: list[list[int]] = field(default_factory=list)

    valid_commands = ("F", "B", "R", "L")

    direction_map = {
        "NORTH": Coordinates(0, 1, "WEST", "EAST"),
        "EAST": Coordinates(1, 0, "NORTH", "SOUTH"),
        "SOUTH": Coordinates(0, -1, "EAST", "WEST"),
        "WEST": Coordinates(-1, 0, "SOUTH", "NORTH"),
    }

    def is_valid_command(self, command: str) -> bool:
        for ch in command:
            if ch not in self.valid_commands:
                return False

        return True

    def is_obstacle(self, x: int, y: int) -> bool:
        return [x, y] in self.obstacles

    def move(self, command: str):
        if not self.is_valid_command(command):
            raise ValueError("invalid command. The rover does not move")

        for ch in command:
            x, y, direction = self._compute_new_coordinates(ch)
            if obstacle := self.is_obstacle(x, y):
                return self._new_coordinates_output(obstacle)

            self._apply_new_coordinates(x, y, direction)

        return self._new_coordinates_output()

    def _new_coordinates_output(self, obstacle: bool = False):
        if obstacle:
            return self.x, self.y, self.direction, "STOPPED"
        return self.x, self.y, self.direction

    def _compute_new_coordinates(self, command: str) -> Tuple[int, int, str]:
        x = self.x
        y = self.y
        direction = self.direction

        if command == "B":
            x -= self.direction_map[self.direction].x
            y -= self.direction_map[self.direction].y
        if command == "F":
            x += self.direction_map[self.direction].x
            y += self.direction_map[self.direction].y
        if command == "R":
            direction = self.direction_map[self.direction].right
        if command == "L":
            direction = self.direction_map[self.direction].left

        return x, y, direction

    def _apply_new_coordinates(self, x: int, y: int, direction: str) -> None:
        self.x = x
        self.y = y
        self.direction = direction
