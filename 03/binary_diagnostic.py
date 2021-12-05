"""--- Day 3: Binary Diagnostic ---

The submarine has been making some odd creaking noises, so you ask it to
produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers
which, when decoded properly, can tell you many useful things about the
conditions of the submarine. The first parameter to check is the power
consumption.

You need to use the binary numbers in the diagnostic report to generate two new
binary numbers (called the gamma rate and the epsilon rate). The power
consumption can then be found by multiplying the gamma rate by the epsilon
rate.

Each bit in the gamma rate can be determined by finding the most common bit in
the corresponding position of all numbers in the diagnostic report. For
example, given the following diagnostic report:

00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010

Considering only the first bit of each number, there are five 0 bits and seven
1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the
second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0,
respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most
common bit, the least common bit from each position is used. So, the epsilon
rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon
rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate
and epsilon rate, then multiply them together. What is the power consumption
of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

DIGITS = 12


def gamma_epsilon(numbers):
    # An array representing the total number of 1s in each place.
    digit_total = [0] * DIGITS
    for number in numbers:
        for i in range(0, DIGITS):
            # Get the digit in the ith place.
            digit = (number & 2 ** i) >> i
            # Will add 1 if digit is 1, etc.
            digit_total[i] += digit
    length = len(numbers)
    # Convert the digit totals to 1s or zeroes depending on if the number in
    # that position is greater than the half the length.
    digit_total = ['1' if x >= length / 2 else '0' for x in digit_total]
    # Need to reverse digit_total since the indices are from the left.
    digit_total = digit_total[::-1]
    gamma = int(''.join(digit_total), 2)
    # XOR gamma to get epsilon.
    epsilon = gamma ^ (2 ** DIGITS - 1)
    return (gamma, epsilon)


if __name__ == '__main__':
    with open('binary_diagnostic_input', 'r') as file:
        numbers = file.readlines()
        numbers = [int(x, 2) for x in numbers]
    values = gamma_epsilon(numbers)
    print(values[0] * values[1])
