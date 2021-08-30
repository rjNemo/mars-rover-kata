import pytest as pytest

from rover.rover import Rover


@pytest.fixture
def rover():
    return Rover(0, 0, "EAST")
