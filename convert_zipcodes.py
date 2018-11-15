#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function


def print_digit(digit):
    """
    Takes a single integer digit and converts it into bars and colons according
    """
    digit = int(digit)
    #print("Passed digit: ", digit)
    if digit == 0:
        return "||:::"

    code = ""
    twobars = 0
    weights = [7, 4, 2, 1, 0]
    for weight in weights:
        if (digit - weight) >= 0 and twobars < 2:
            code += "|"
            digit -= weight
            twobars += 1
        else:
            code += ":"
    #print("Code: ", code)
    return code


def print_barcode(zipcode):
    """
    placeholder
    """
    if not zipcode.isdigit():
        print("Error:", zipcode, "is not all numbers")
        return
    if len(zipcode) != 5:
        print("Error: Zipcodes need to be exactly 5 digits long! \n      ",
              zipcode, "is not 5 digits long!")
        return


    barcode = "|"

    #barcode += ''.join([print_digit(digit) for digit in zipcode])

    for digit in zipcode:
        barcode += " (" + print_digit(digit) + ")"

    print("Zipcode: ", zipcode)

    digits_sum = sum([int(i) for i in zipcode])
    check = (10 - (digits_sum % 10)) % 10
    print("Check Number: ", check)

    barcode += " (" + print_digit(check) + ") |"
    print(barcode)


def main():
    """
    Test your module
    """
    print_barcode("01234")
    print_barcode("36924")
    print_barcode("2c34a")
    print_barcode("123456")


if __name__ == "__main__":
    main()
    exit(0)
