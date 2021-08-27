import dataclasses


@dataclasses.dataclass
class Rover:
    x: int
    y: int
    direction: str

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

    def move(self, command: str):
        if not self.is_valid_command(command):
            raise ValueError("invalid command. The rover does not move")

        for ch in command:
            self._move_one_step(ch)

        return self.x, self.y, self.direction

    def _move_one_step(self, command):
        if command == "B":
            self.x -= self.direction_map[self.direction][0]
            self.y -= self.direction_map[self.direction][1]
        if command == "F":
            self.x += self.direction_map[self.direction][0]
            self.y += self.direction_map[self.direction][1]
        if command == "R":
            self.direction = self.direction_map[self.direction][3]
        if command == "L":
            self.direction = self.direction_map[self.direction][2]
