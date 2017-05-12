#tested with phthon 3.4 on windows 8

import serial
import time

#################################
SERIAL_PORT="COM19"
LOG_FILE_PATH="serial_log.txt"
BAUD=115200
#################################

LOG_FILE=None

def log(s):
        print(s,end='')
        if LOG_FILE:
                LOG_FILE.write(s)

#main        
if __name__ == '__main__':
        #handle ctrl-c
        try:
                #handle file open issue
                with open(LOG_FILE_PATH, "a") as LOG_FILE:
                        serial_port = serial.Serial(
                                SERIAL_PORT,
                                timeout=None,
                                baudrate=BAUD)
                    
                        #close first...
                        serial_port.close()
                    
                        try:
                                serial_port.open()
                        
                                #serial_port.close()
                        except:
                                print("error: com port open failed")
                                serial_port.close()
                                exit()
                    
                        print("CONNECT SUCCESS")


                        last_is_newline=True
                        while True:
                                b = serial_port.inWaiting()
                                r = serial_port.read(1)
                                if len(r):
                                        try:
                                                #print(r)
                                                if last_is_newline:
                                                        #print(time.strftime("[%Y/%m/%d_%H:%M:%S]: "), end='')
                                                        LOG_FILE.flush()
                                                        log(time.strftime("[%Y/%m/%d_%H:%M:%S]: "))
                                                l=r.decode('ASCII')
                                                
                                                #print(l, end='')
                                                log(l)

                                                last_is_newline = (l == "\n")                                        

                                        except:
                                                print("decode error")
        except KeyboardInterrupt:
                print("Bye~~")
                serial_port.close()
                LOG_FILE.close()
                exit()
        
    
    
    
