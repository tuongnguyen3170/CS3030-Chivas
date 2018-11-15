#!/usr/bin/env python3


from urllib.request import urlopen
from tuong_nguyen_task1_hw7 import doorCheck

def run_test():
  """
  This function will call the function doorCheck from
  Module 1 to check the validity of the doors' signal
  """
  my_list = []
  with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv") as f:
       for row in f:
         #Reading the decode line, and also remove spaces
         lines = row.decode('utf-8').strip().replace(" ","").split(",")
         #Add lines to list my_list
         my_list.append(lines)
  for i in range(1,len(my_list)):
    print("==> READING RECORD #"+str(i))
    doorCheck(my_list[i][1],my_list[i][2],my_list[i][3],my_list[i][4],
              my_list[i][5],my_list[i][6],my_list[i][7],my_list[i][8],
              my_list[i][9])
def main():
  """
  Run test
  """
  run_test()

if __name__ == '__main__':
  main()

