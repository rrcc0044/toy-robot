from robot import Robot


def test_without_initial_place():
    robot = Robot()
    robot.move()

    assert robot.coordinates == (0, 1)
    assert robot.direction == 'NORTH'


def test_with_initial_place():
    robot = Robot()
    robot.coordinates = (1, 2)
    robot.direction = 'EAST'
    robot.move()
    robot.move()
    robot.turn_left()
    robot.move()

    assert robot.coordinates == (3, 3)
    assert robot.direction == 'NORTH'


def test_with_ignored_invalid_move():
    robot = Robot()
    robot.turn_left()
    robot.move()
    robot.move()
    robot.move()
    robot.turn_right()
    robot.move()

    assert robot.coordinates == (0, 1)
    assert robot.direction == 'NORTH'


def test_robot_left_turns():
    robot = Robot()

    for _ in range(15):
        robot.turn_left()

    assert robot.coordinates == (0, 0)
    assert robot.direction == 'EAST'


def test_robot_right_turns():
    robot = Robot()

    for _ in range(15):
        robot.turn_right()

    assert robot.coordinates == (0, 0)
    assert robot.direction == 'WEST'
