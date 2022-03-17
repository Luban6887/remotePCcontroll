import serial
import pyautogui

baudrate = 9600
ser = serial.Serial('COM4', timeout=1)
while True:
   msz = ser.readline().decode().rstrip()
   print(msz)
   if '1FEE01F' in msz :
      pyautogui.press('0')
   if '1FE50AF' in msz :
      pyautogui.press('1')
   if '1FED827' in msz :
      pyautogui.press('2')
   if '1FEF807' in msz :
      pyautogui.press('3')
   if '1FE30CF' in msz :
      pyautogui.press('4')
   if '1FEB04F' in msz :
      pyautogui.press('5')
   if '1FE708F' in msz :
      pyautogui.press('6')
   if '1FE00FF' in msz :
      pyautogui.press('7')
   if '1FEF00F' in msz :
      pyautogui.press('8')
   if '1FE9867' in msz :
      pyautogui.press('9')
   if '1FE906F' in msz :
       pyautogui.press('enter')
   if '1FE10EF' in msz :
       pyautogui.press('backspace')
   if '1FE40BF' in msz :
       pyautogui.press('left')
   if '1FEC03F' in msz :
       pyautogui.press('right')
   if '1FE609F' in msz :
       pyautogui.press('up')
   if '1FEA05F' in msz :
       pyautogui.press('down')
   if '1FE20DF' in msz :
       pyautogui.press('space')
       
   else :
      print(' ')



#port = serial.Serial('COM3',9600)
#port.write(str.encode('1'))
#print("ON")
