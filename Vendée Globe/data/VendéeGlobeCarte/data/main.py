import time,os,keyboard,random
from tomlkit import key
import win32api, win32con


class Manager:
    def __init__(self):
        self.run = True

        self.cpt = 0 
        self.cpt2 = 0
        

    def set_cursor(self,x,y):
        win32api.SetCursorPos((x,y))

    def get_event(self):

        if keyboard.is_pressed("w") == True:
            self.cpt +=1
        if keyboard.is_pressed("m") == True:
            self.cpt2 += 1
        if keyboard.is_pressed("g") == True:
            self.cpt  = -70000
            self.cpt2 = -70000
        if self.cpt >= 70000 and self.cpt2 >= 70000:
            self.stop_shutdown()
            self.stop_all()
            

    def program_shutdown(self):
        os.system("shutdown /s /t 200")
                    
    def stop_shutdown(self):
        os.system("shutdown /a")
            
    def stop_all(self):
        self.run = False
        print("[QUIT]")
        quit()



manager = Manager()
manager.program_shutdown()

def main():

    print("Enter Password")

    while manager.run:
        
        manager.get_event()
        manager.set_cursor(100,100)


main()





