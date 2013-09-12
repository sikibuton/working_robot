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
import array

def main():
    os.system("echo ttyO1_armhf.com > /sys/devices/bone_capemgr.9/slots")
    ser = serial.Serial("/dev/ttyO1",baudrate = 9600)
    terget = 1500 #unit is us
    channel = 0
    data = terget*4
    send_list = [0x84]
    send_list.append(channel)
    send_list.append(data & 0x7f)
    send_list.append((data>>7)&0x7f)
    ser.write(array.array('B',send_list))


    ser.write("hello")

if __name__ == '__main__':
    main()
