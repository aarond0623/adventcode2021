"""--- Day 2: Dive! ---

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down
2, or up 3:

    - forward X increases the horizontal position by X units.
    - down X increases the depth by X units.
    - up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so
they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You
should probably figure out where it's going. For example:

forward 5 down 5 forward 8 up 3 down 8 forward 2

Your horizontal position and depth both start at 0. The steps above would then
modify them as follows:

    - forward 5 adds 5 to your horizontal position, a total of 5.
    - down 5 adds 5 to your depth, resulting in a value of 5.
    - forward 8 adds 8 to your horizontal position, a total of 13.
    - up 3 decreases your depth by 3, resulting in a value of 2.
    - down 8 adds 8 to your depth, resulting in a value of 10.
    - forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15
and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the
planned course. What do you get if you multiply your final horizontal position
by your final depth?
"""
from math import prod


def control(position, command):
    """Performs a submarine command based on a string.

    The submarines position is represented as a tuple (x, y) with x
    representing the horizontal position, and y representing the depth, where y
    increases with depth.

    Args:
        position: The current position of the submarine.
        command: A string with a command (forward, up, down) followed by a
            distance.

    Returns:
        A tuple representing the submarine's new position.
    """
    # Translation data
    controls = {
        'forward': (1, 0),
        'down': (0, 1),
        'up': (0, -1)
    }
    command = command.split()
    control = controls[command[0]]
    distance = int(command[1])
    # Get the total translation.
    movement = tuple([x * distance for x in control])
    # Add it to the original position.
    return tuple([x + y for x, y in zip(position, movement)])


def main():
    # Define a tuple for horizontal position and depth.
    position = (0, 0)
    with open('dive_input', 'r') as file:
        for line in file:
            position = control(position, line)
    # Multiply the horizontal position and the height and return.
    return prod(position)


if __name__ == '__main__':
    print(main())
