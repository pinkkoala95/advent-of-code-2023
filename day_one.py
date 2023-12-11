# Press ⌃R to execute it or replace it with your code.
import re


def findCalibrationValue():
    output = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = {"zero": "0", "one": "1",
                      "two": "2", "three": "3",
                      "four": "4", "five": "5",
                      "six": "6", "seven": "7",
                      "eight": "8", "nine": "9",
                      "0": "0", "1": "1", "2": "2",
                      "3": "3", "4": "4", "5": "5",
                      "6": "6", "7": "7", "8": "8",
                      "9": "9"
                      }

    input = open("day_one_input.txt", "r+")

    for line in input:
        for number in numbers:
            if number in line:
                line.replace(number, numbers[number])

        numbersOnLine = ''.join(char for char in line if char not in alphabet).replace('\n', '')

        if len(numbersOnLine) == 2:
            output += int(numbersOnLine)
            print("output", output)
        else:
            twoDigitNumber = numbersOnLine[0] + numbersOnLine[-1]
            output += int(twoDigitNumber)
            print("output", output)

    print(output)
    return


if __name__ == '__main__':
    findCalibrationValue()
