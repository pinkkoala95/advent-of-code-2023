# Press ⌃R to execute it or replace it with your code.

def findCalibrationValue():
    output = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    input = open("day_one_input.txt", "r")
    for line in input:
        numbersOnLine = ''.join(char for char in line if char not in alphabet).replace('\n', '')

        if len(numbersOnLine) == 2:
            output += int(numbersOnLine)
        else:
            twoDigitNumber = numbersOnLine[0] + numbersOnLine[-1]
            output += int(twoDigitNumber)
    print(output)
    return

if __name__ == '__main__':
    findCalibrationValue()

