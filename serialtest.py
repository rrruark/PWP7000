# Robert Ruark
# 05/13/2023
#
# PWP7000LT Daisy Wheel Printer 'Driver'
# 
# This printer accepts ASCII text over 1200 baud serial. Most printable characters are supported.

import serial
import time
import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument("-p","--port", help="Defines serial port. COM20 by default.", default="COM20")
parser.add_argument("-f","--file", help="Defines file to be printed.", default="test.txt")

args = parser.parse_args()

print(args.port)

ser = serial.Serial(args.port, 1200, timeout=0, rtscts=True,dsrdtr=True)
ser.write(b'\r\n')
with open(args.file) as f:
    linenum=1
    for line in f:
        words=line.split()
        n=1
        for word in words:
            if(word == "1/2"):
                word = "|"
            if(word == "1/4"):
                word = "}"
            if(n+len(word)>70):
                if(linenum==55):
                    variable = input('Please insert a new sheet of paper when printing completes and press any key to continue: ')
                    linenum=1
                ser.write(b'\r\n')
                ser.write(word.encode('utf-8'))
                ser.write(b' ')
                n=2+1+len(word)
                linenum+=1
            else:
                ser.write(word.encode('utf-8'))
                ser.write(b' ')
                n+=1+len(word)
        linenum+=1
    ser.write(b'\f')
time.sleep(10) #Required so the port doesn't close too early.
ser.write(b'\r\n')
ser.close()             # close port