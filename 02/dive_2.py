"""--- Part Two ---

Based on your calculations, the planned course doesn't seem to make any sense.
You find the submarine manual and discover that the process is actually
slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third
value, aim, which also starts at 0. The commands also mean something entirely
different than you first thought:

    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    - forward X does two things:
        - It increases your horizontal position by X units.
        - It increases your depth by your aim multiplied by X.

Again note that since you're on a submarine, down and up do the opposite of
what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

    - forward 5 adds 5 to your horizontal position, a total of 5. Because your
      aim is 0, your depth does not change.
    - down 5 adds 5 to your aim, resulting in a value of 5.
    - forward 8 adds 8 to your horizontal position, a total of 13. Because your
      aim is 5, your depth increases by 8*5=40.
    - up 3 decreases your aim by 3, resulting in a value of 2.
    - down 8 adds 8 to your aim, resulting in a value of 10.
    - forward 2 adds 2 to your horizontal position, a total of 15. Because your
      aim is 10, your depth increases by 2*10=20 to a total of 60.

After following these new instructions, you would have a horizontal position of
15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal
position and depth you would have after following the planned course. What do
you get if you multiply your final horizontal position by your final depth?
"""
from math import prod


class Submarine:
    """A submarine that moves through the water.

    The submarine's current position is defined by a tuple, (x, y), in which x
    is an integer representing the submarine's horizontal position, and y is an
    integer representing the depth, with y increasing with depth.
    """
    def __init__(self, x, y):
        self.position = (x, y)
        # Aim is an integer representing how much the submarine will dive
        # relative to the foward movement when the submarine moves forward.
        self.aim = 0

    def control(self, command):
        """Controls the submarine.

        Commands are given with a string and an integer.

        Args:
            command: A command for the submarine. Can be one of three things:
                down X: Increases the submarine's aim by X.
                up X: Decreases the submarine's aim by X.
                forward X: Moves the submarine forward by X and changes the
                    depth by X * aim.
        """
        # Controls are tuples representing the effect on position and aim.
        controls = {
            'forward': (1, 0),
            'down': (0, 1),
            'up': (0, -1)
        }
        command = command.split()
        control = controls[command[0]]
        distance = int(command[1])
        self.aim += distance * control[1]
        movement = (distance * control[0], distance * control[0] * self.aim)
        self.position = tuple([x + y for x, y in zip(self.position, movement)])


def main():
    # Initialize the submarine.
    sub = Submarine(0, 0)
    with open('dive_input', 'r') as file:
        for line in file:
            sub.control(line)
    # Multiply the horizontal position and the height and return.
    return prod(sub.position)


if __name__ == '__main__':
    print(main())
