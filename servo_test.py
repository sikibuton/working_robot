#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      koki
#
# Created:     12/09/2013
# Copyright:   (c) koki 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import serial

def main():
    os.system("echo ttyO1_armhf.com > /sys/devices/bone_capemgr.9/slots")
    ser = serial.Serial("/dev/ttyO1",baudrate =9600)
    ser.write("hello")

if __name__ == '__main__':
    main()
