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
import time

class servo:
      def __init__(self,minus90_us,plus90_us,max_limit_degree,min_limit_degree):
        self.minus90_us = minus90_us
        self.plus90_us = plus90_us
        self.terget = (self.plus90_us+self.minus90_us)/2 #us
        self.max_limit_degree = max_limit_degree
        self.min_limit_degree = min_limit_degree
      def set_angle(self,degree):
          if self.max_limit_degree < degree:
             degree = self.max_limit_degree
          if self.min_limit_degree > degree:
             degree = self.min_limit_degree



def main():
	os.system("echo ttyO1_armhf.com > /sys/devices/bone_capemgr.9/slots")
	ser = serial.Serial("/dev/ttyO1",baudrate = 9600)
	terget = 800
	while 1:
		terget += 20
		if terget >= 1700:
			terget = 800
		channel = 0
		data = terget*4
		send_list = [0x84]
		send_list.append(channel)
		send_list.append(data & 0x7f)
		send_list.append((data>>7)&0x7f)
		ser.write(array.array('B',send_list).tostring())
		print(array.array('B',send_list).tostring())
		time.sleep(0.20)



if __name__ == '__main__':
    main()
