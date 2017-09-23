### * ------------------------------------------------------------------ *
### * Jika Error lakukan langkah berikut :								
### * 1. Periksa "max user watch" dengan perintah : cat /proc/sys/fs/inotify/max_user_watches
### * 2. SET "max user watch" dengan perintah (Tidak Permanen) : sudo sysctl fs.inotify.max_user_watches=16384
### * 3. SET "max user watch" dengan perintah (Permanen) : echo 16384 | sudo tee -a /proc/sys/fs/inotify/max_user_watches
### * Sumber : https://stackoverflow.com/questions/27948612/django-test-run-environment-error-no-enough-space-left-on-disk 
### * Sumber : https://askubuntu.com/questions/154255/how-can-i-tell-if-i-am-out-of-inotify-watches
### * ------------------------------------------------------------------ *

### * ---------------------- *
### * ini untuk Linux System *
### * ---------------------- *

### * Intall Module Depend-------- *
### * sudo apt install python-pip
### * pip install pyinotify
### * pip install psutil
### * pip install termcolor
### * ---------------------------- *

import pyinotify
import sys
import os

import psutil

# Module untuk handle time 
import datetime
import time

#Modul untuk Warna
from termcolor import colored, cprint

# Daftar WARNA colored : 
## Text_Colors : yellow, magenta, cyan, red, blue, white, grey, green
## Text_highlights : on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white
## Attributes : bold, dark, underline, blink, reverse, concealed
## Sumber : https://pypi.python.org/pypi/termcolor

# use tm and d1 as global variable not give real time
## tm = time.time()	
## d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')

log_path = os.getcwd() 
log_file = "ActionsREC.LOG"

class ShowEvent(pyinotify.ProcessEvent):
    #global d1, # use d1 as global variable not give real time
    
    global log_file
    def file_event(self,act, event,clr): # ini Experiment
        global log_file	
        try:
            tm = time.time()	
            d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S:%f')[:-4]
            if not log_file in event.pathname: # disable baris ini jika gunakan exclude_filter (masih errror) 
                d2 = d1+" : " + act + " : " + event.pathname
                if len(sys.argv) >= 2:
                    if sys.argv[1].strip() == "off" or sys.argv[1].strip() == "OFF":				
                        offrec = colored("OFF_REC : ","red")+colored(d2,clr)
                        print(offrec)
                else:
                    write_2log(log_file,d2)
                    cprint(d2,clr)					
                #print colored(d2,clr)
                #cprint(d2,clr,attrs=['bold']) # Cetak Tebal 
                #cprint(d2,clr,'on_grey') # Warna Latar : on_grey
                #cprint(d2,clr)			
        except:
            cprint('---------ERROR-Cannot Watch !--------','white','on_blue')
            pass
			
    def process_IN_ACCESS(self, event):
        self.file_event('ACCESS__EVENT',event,'cyan')

    def process_IN_ATTRIB(self, event):
        self.file_event('ATTRIB__EVENT',event,'white')

    def process_IN_CLOSE_NOWRITE(self, event):
        self.file_event('CLOSE_NoWRITE',event,'magenta') #CLOSE_NOWRITE

    def process_IN_CLOSE_WRITE(self, event):
        self.file_event('CLOSE___WRITE',event,'magenta') #CLOSE_WRITE  				

    def process_IN_CREATE(self, event):
        self.file_event('CREATE__EVENT',event,'green')   				

    def process_IN_DELETE(self, event):
        self.file_event('DELETE__EVENT',event,'red')
		
    def process_IN_MODIFY(self, event):
        self.file_event('MODIFY__EVENT',event,'cyan')
		
    def process_IN_OPEN(self, event):
        self.file_event('OPEN____EVENT',event,'magenta')		

    def process_IN_MOVED_FROM(self,event):
        self.file_event('RENAME___From',event,'yellow') # MOVED From or RENAME FROM

    def process_IN_MOVED_TO(self,event):
        self.file_event('RENAME___To__',event,'yellow')# MOVED To or RENAME TO		
		
def write_2log(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
		f.close

def main():
    global log_path, log_file

    log = colored('Enable','green')
    if len(sys.argv) >= 2:
        if sys.argv[1].strip() == "off" or sys.argv[1].strip() == "OFF":
            log = colored('Disable','red')

    print ('''-------------------------
 input folder to watch, support multi-folder,
 write log\t: '''+log+'''
 log file\t: '''+colored(log_file,'green')+'''
 log path\t: '''+colored(log_path,'green')+'''
 example input\t: (Folder to Watch : /var/log /home /mnt)
-------------------------''')
    path = raw_input("Folder to Watch : ")
    path = path.split()
    #exlist = [log_file,other_log_file] ## exclude_filter masih Error, belum bisa digunakan 
    #exclist = pyinotify.ExcludeFilter(exlist)
    if path[0] == "x" or path[0] == "X":	
        exit()

    for xdir in path:
        if not os.path.isdir(xdir):
            cprint('Bukan DIR : '+xdir,'red')
            exit()

    if path !="":
        # watch manager
        wm = pyinotify.WatchManager()
        #wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True, exclude_filter=exclist) # Not Working
        wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True)

        # event handler
        eh = ShowEvent()

        # notifier
        notifier = pyinotify.Notifier(wm, eh)
        notifier.loop()

if __name__ == '__main__':
    main()
