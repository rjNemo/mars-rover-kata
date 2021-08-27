import pytest

from rover.rover import Rover


def test_rover_initialisation():
    assert Rover(0, 0, "EAST")


def test_rover_can_move(rover):
    command = "F"
    assert rover.move(command) is not None


@pytest.mark.parametrize(
    ("init", "command", "expected"),
    [
        ((0, 0, "EAST"), "F", (1, 0, "EAST")),
        ((0, 0, "EAST"), "B", (-1, 0, "EAST")),
        ((0, 0, "EAST"), "R", (0, 0, "SOUTH")),
        ((0, 0, "EAST"), "L", (0, 0, "NORTH")),
        # change starting point
        ((0, 0, "WEST"), "F", (-1, 0, "WEST")),
        ((0, 0, "SOUTH"), "R", (0, 0, "WEST")),
        ((0, 0, "SOUTH"), "F", (0, -1, "SOUTH")),
    ],
)
def test_rover_receive_commands(init, command, expected):
    rover = Rover(*init)
    assert rover.move(command) == expected


def test_rover_rejects_invalid_commands(rover):
    command = " W "
    with pytest.raises(ValueError):
        rover.move(command)


@pytest.mark.parametrize(
    ("init", "command", "expected"),
    [
        ((0, 0, "NORTH"), "FB", (0, 0, "NORTH")),
        ((0, 0, "NORTH"), "FF", (0, 2, "NORTH")),
        ((4, 2, "EAST"), "FLFFFRFLB", (6, 4, "NORTH")),
    ],
)
def test_rover_can_receive_multiple_commands(init, command, expected):
    rover = Rover(*init)
    assert rover.move(command) == expected
