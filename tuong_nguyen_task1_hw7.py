#!/usr/bin/env python3
"""
This module used to test the condition to unlock the car doors
"""

def doorCheck(LD, RD, CL, ML, LI, LO, RI, RO, GS):
     """
     This function use to check the cases when the doors are locked
     or opened.
     :param:
          LD: left door
          RD: right door
          CL: Child lock
          ML: master lock
          LI: left inside door
          LO: left outside door
          RI: right inside door
          RO: right outside door
          GS: gear shift
     """
     print("Left dashboard switch (0 or 1):", LD)
     print("Right dashboard switch (0 or 1):", RD)
     print("Child lock switch (0 or 1):", CL)
     print("Master unlock switch (0 or 1):", ML)
     print("Left inside handle (0 or 1):", LI)
     print("Left outside handle (0 or 1):", LO)
     print("Right inside handle (0 or 1):", RI)
     print("Right outside handle (0 or 1):", RO)
     print("Gear shift position (P, N, D, 1, 2, 3 or R):", GS)
     print()

     #Cases check
     if GS not in {'P', 'p', 'N', 'n', 'D', 'd', '1', '2', '3', 'R'}:
          print("INVALID RECORD: ALL DOORS STAY CLOSED.")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif GS == 'R' or GS == 'D' or GS == 'N' or GS == 'r' or GS == 'd' or GS == 'n' or GS == '1' or GS == '2' or GS == '3' :
           print ("BOTH DOORS ARE CLOSED")
           print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif LO == '1' and ML == '1' and GS == 'P' or GS == 'p' and RO == '1' and RD == '1' and LD == '1' and RI == '1' and LI == '1' and CL == '1' :
           print ("BOTH DOORS ARE OPEN")
           print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif ML == '0' and GS == 'P' or GS == 'p' and LD == '0' and RD == '0' and LI == '0' and RI == '0' and LO == '0' and RO == '0' and CL == '0' :
           print ("BOTH DOORS ARE CLOSE")
           print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")


     elif LD == '1' and ML == '1' and GS == 'P' or GS == 'p' and RD == '0' and LI == '0' and RI == '0' and LO == '0' and RO == '0' and CL == '0' :
          print ("LEFT SIDE DOOR IS OPEN ")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif RD == '1' and ML == '1' and GS == 'P' or GS == 'p' and LD == '0' and LI == '0' and RI == '0' and LO == '0' and RO == '0' and CL == '0' :
          print ("RIGHT SIDE DOOR IS OPEN ")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif LI == '1' and ML == '1' and GS == 'P' or GS == 'p' and RI == '0' and RD == '0' and LD == '0' and LO == '0' and RO == '0' and CL == '0' :
          print ("LEFT SIDE DOOR IS OPEN ")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif RI == '1' and ML == '1' and GS == 'P' or GS == 'p' and LI == '0' and RD == '0' and LD == '0' and LO == '0' and RO == '0' and CL == '0' :
          print ("RIGHT SIDE DOOR IS OPEN ")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_")

     elif RO == '1' and ML == '1' and GS == 'P' or GS == 'p' and LO == '0' and RD == '0' and LD == '0' and RI == '0' and LI == '0' and CL == '0' :
          print ("RIGHT SIDE DOOR IS OPEN")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")

     elif LO == '1' and ML == '1' and GS == 'P' or GS == 'p' and RO == '0' and RD == '0' and LD == '0' and RI == '0' and LI == '0' and CL == '0' :
          print ("LEFT SIDE DOOR IS OPEN ")
          print ("+_+_+_+_+_+_+_+_+_+_+_+_\n")
