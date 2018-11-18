#!/usr/bin/env python3
"""
Module Documentation Here
"""
from __future__ import print_function
from urllib.request import urlopen
import jordan_stong_task3_hw7 as convert_zipcode



def main():
    """
    Retrieves an online file containing zipcodes and feeds them to
    module 3 (conver_zipcode) to convert the zipcodes into barcodes
    """
    with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt") as zipcodes:
        for zipcode in zipcodes:
            zipcode = zipcode.decode('utf-8').strip()
            #print(zipcode)

            convert_zipcode.print_barcode(zipcode)



if __name__ == "__main__":
    main()
    exit(0)
