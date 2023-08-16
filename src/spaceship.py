class Spaceship:
    def __init__(self, x=0, y=0, z=0, direction="N"):
        self.position = (x, y, z)
        self.direction = direction

    def move_forward(self):
        if self.direction == "N":
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == "S":
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == "E":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == "W":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == "Up":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)
        elif self.direction == "Down":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)

    def move_backward(self):
        if self.direction == "N":
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == "S":
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == "E":
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == "W":
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == "Up":
            self.position = (self.position[0], self.position[1], self.position[2] - 1)
        elif self.direction == "Down":
            self.position = (self.position[0], self.position[1], self.position[2] + 1)

    def turn_left(self):
        directions = ["N", "W", "S", "E", "Up", "Down"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % len(directions)]

    def turn_right(self):
        directions = ["N", "E", "S", "W", "Down", "Up"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % len(directions)]

    def turn_up(self):
        directions = ["Up", "N", "Down", "S", "E", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % len(directions)]

    def turn_down(self):
        directions = ["Down", "S", "Up", "N", "E", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % len(directions)]

    def execute_command(self, command):
        if command == "f":
            self.move_forward()
        elif command == "b":
            self.move_backward()
        elif command == "l":
            self.turn_left()
        elif command == "r":
            self.turn_right()
        elif command == "u":
            self.turn_up()
        elif command == "d":
            self.turn_down()

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction
