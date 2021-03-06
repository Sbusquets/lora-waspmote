#-*- coding: utf-8 -*-
'''
  Comunicació serial Waspmote SX1272 (gateway)
  http://www.libelium.com/development/waspmote/documentation/lora-gateway-tutorial/

  TLDR: Continuously listen serial port and handle output, i.e packets sent by lora transmitter

'''
import time
import serial
import config            as c # see 'config.py'
import processa_missatge as p # see 'processa_missatge.py'

#nova connexió serial
ser          = serial.Serial()
ser.port     = c.port
ser.baudrate = c.baudrate
ser.bytesize = c.bytesize
ser.parity   = c.parity
ser.stopbits = c.stopbits
ser.timeout  = c.timeout
ser.open()
ser.flush()

#funció listen
def listen():
  print('Escoltant a',ser.port);
  try:
    while True:
      if(ser.in_waiting):
        rebut=ser.read(ser.in_waiting);
        try:
          p.processa(rebut);
        except Exception as e:
          print(e);
      else:
        time.sleep(5); #wait some time so input buffer can be filled
  except KeyboardInterrupt:
    pass;

#listen serial port
listen()
