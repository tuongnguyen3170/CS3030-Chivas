# CS3030-Chivas
Tuong Nguyen
Module 1:
  This module 1 used to set the conditions for the car doors to open
  The function doorCheck will be used to check all the different combinations
  to open or close the doors. 
  This function will accept 9 parameters, which represent for:
    Left dashboard switch (LD)
    Right dashboard switch (RD)
    Child lock switch (CL)
    Master unlock switch (ML)
    Left inside handle (LI)
    Left outside handle (LO)
    Right inside handle (RI)
    Right outside handle (RO)
    Gear shift position (GS): Valid Fields: P, N, D, 1, 2, 3 or R

 Module 2:
   This module will receive the data file from the URL.
   It will read in the data and use it to check the conditions in module 1
   The function run_test will take and process the data, using the doorCheck 
   funtion from module 1.
 
Module 3:
    This module recieves a zipcode in as a parameter and converts it into a 
    barcode that it prints out. The zipcode should be 5 digits long and only
    contain numbers

Module 4:
    This module reads a URL file containing zipcodes. It then feeds these
    zipcodes to Module 3 to be converted into barcodes:w

