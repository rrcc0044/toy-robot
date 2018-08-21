directions = ('NORTH', 'EAST', 'SOUTH', 'WEST')
coordinates = {
    'NORTH': (0, 1),
    'EAST': (1, 0),
    'WEST': (-1, 0),
    'SOUTH': (0, -1),
}


class Robot:
    def __init__(self, direction='NORTH', coordinates=(0, 0), board_size=5):
        self.direction = direction
        self.coordinates = coordinates
        self.board_size = 5

    def turn_left(self):
        index = directions.index(self.direction) - 1
        self.direction = directions[index]

    def turn_right(self):
        index = directions.index(self.direction) + 1
        index = index if len(directions) > index else 0
        self.direction = directions[index]

    def move(self):
        coordinate = coordinates.get(self.direction)
        temp = tuple(map(sum, zip(coordinate, self.coordinates)))

        if self.board_size in temp or -1 in temp:
            return

        self.coordinates = temp

    def report(self):
        x = self.coordinates[0]
        y = self.coordinates[1]
        print(f'Output: {x},{y},{self.direction}')


if __name__ == "__main__":

    command_map = {
        'LEFT': Robot.turn_left,
        'RIGHT': Robot.turn_right,
        'MOVE': Robot.move,
        'REPORT': Robot.report,
    }

    robot = Robot()

    while True:
        command = input("Enter command: ").upper()

        if 'PLACE' in command:
            args = command.split(" ")[1].split(",")
            robot.direction = args[2]
            robot.coordinates = tuple(map(int, args[:2]))
        else:
            command_map[command](robot)
