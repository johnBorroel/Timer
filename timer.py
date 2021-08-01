import time
import winsound

class Timer:
    def __init__(self, hours:int = 0, minutes:int = 1, seconds:int = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    def start(self):
        while True:
            timer = '{:02d}:{:02d}:{:02d}'.format(self.hours,
                                                  self.minutes,
                                                  self.seconds
                                                  )
            print(timer, end='\r')

            time.sleep(1)
            if self.seconds == 0:
                if self.minutes == 0:
                    if self.hours == 0:
                        break
                    else:
                        self.hours -= 1
                        self.minutes = 59
                        self.seconds = 59
                else:
                    self.minutes -= 1
                    self.seconds = 59
            else:
                self.seconds -= 1
            
        print('Timer done!')
        winsound.Beep(500,500)
