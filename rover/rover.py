import dataclasses


@dataclasses.dataclass
class Rover:
    x: int
    y: int
    direction: str
    obstacles: list[list[int]] = dataclasses.field(default_factory=list)

    valid_commands = ("F", "B", "R", "L")

    direction_map = {
        "NORTH": (0, 1, "WEST", "EAST"),
        "EAST": (1, 0, "NORTH", "SOUTH"),
        "SOUTH": (0, -1, "EAST", "WEST"),
        "WEST": (-1, 0, "SOUTH", "NORTH"),
    }

    def is_valid_command(self, command):
        for ch in command:
            if ch not in self.valid_commands:
                return False

        return True

    def is_obstacle(self, x: int, y: int):
        return [x, y] in self.obstacles

    def move(self, command: str):
        if not self.is_valid_command(command):
            raise ValueError("invalid command. The rover does not move")

        for ch in command:
            x, y, direction = self._compute_new_coordinates(ch)
            if obstacle := self.is_obstacle(x, y):
                return self.new_coordinates_output(obstacle)

            self.apply_new_coordinates(x, y, direction)

        return self.new_coordinates_output()

    def new_coordinates_output(self, obstacle: bool = False):
        if obstacle:
            return self.x, self.y, self.direction, "STOPPED"
        return self.x, self.y, self.direction

    def _compute_new_coordinates(self, command):
        x = self.x
        y = self.y
        direction = self.direction

        if command == "B":
            x -= self.direction_map[self.direction][0]
            y -= self.direction_map[self.direction][1]
        if command == "F":
            x += self.direction_map[self.direction][0]
            y += self.direction_map[self.direction][1]
        if command == "R":
            direction = self.direction_map[self.direction][3]
        if command == "L":
            direction = self.direction_map[self.direction][2]

        return x, y, direction

    def apply_new_coordinates(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
