#! /usr/bin/env python
# coding: utf-8

import serial
import serial.tools.list_ports
import re

string = "Smartcam ready!"
smartcam_flag = False

comlist = serial.tools.list_ports.comports()
connected = []


def connect_to_cam(port):
    ser = serial.Serial(port, 9600, timeout=1)

    while True :
        line = ser.readline()
        print (line)
        dec_line = line.decode("ascii","ignore")
        print (dec_line)
        if dec_line.find(string):
            print ('Find Smartcam and ready to work!')
            smartcam_flag = True
        if smartcam_flag == True:
            ser.write(input().encode("ascii","ignore"))


for element in comlist:
  connected.append(element.device)
  print (element.device)
  if element.device != '/dev/ttyS0':
    connect_to_cam(element.device)
  else:
    print('Ignore /dev/ttyS0...')
