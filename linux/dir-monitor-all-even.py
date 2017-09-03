import pyinotify

# Module untuk handle time 
import datetime
import time

#Modul untuk Warna
from termcolor import colored

# Daftar WARNA : 
## colored : yellow, magenta, cyan, red, blue, white

# use tm and d1 as global variable not give real time
## tm = time.time()	
## d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')

class ShowEvent(pyinotify.ProcessEvent):
    #global d1, 
    def process_IN_ACCESS(self, event):
        tm = time.time()	#declare var here give real time 
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')	
        print colored(d1+" : ACCESS \t\t:" + event.pathname,'magenta')

    def process_IN_ATTRIB(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')	
        print colored(d1+" : ATTRIB \t\t:" + event.pathname,'white')

    def process_IN_CLOSE_NOWRITE(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')
        print colored(d1+" : CLOSE_NOWRITE \t:" + event.pathname,'white')

    def process_IN_CLOSE_WRITE(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')	
        print colored(d1+" : CLOSE_WRITE \t:" + event.pathname,'magenta')

    def process_IN_CREATE(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')	
        print colored(d1+" : CREATE \t\t:" + event.pathname,'green')

    def process_IN_DELETE(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')		
        print colored(d1+" : DELETE \t\t:" + event.pathname,'red')

    def process_IN_MODIFY(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')		
        print colored(d1+" : MODIFY \t\t:" + event.pathname,'cyan')

    def process_IN_OPEN(self, event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')		
        print colored(d1+" : OPEN \t\t:" + event.pathname,'magenta')

    def process_IN_MOVED_FROM(self,event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')		
        print colored(d1+" : RENAME FROM \t:" + event.pathname,'yellow')

    def process_IN_MOVED_TO(self,event):
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')		
        print colored(d1+" : RENAME TO \t:" + event.pathname,'yellow')
		
def write_2log(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
	f.close

def main():
    # watch manager
    path = raw_input("Folder to Watch : ")
    if path !="":

        wm = pyinotify.WatchManager()
        wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True)

        # event handler
        eh = ShowEvent()

        # notifier
        notifier = pyinotify.Notifier(wm, eh)
        notifier.loop()

if __name__ == '__main__':
    main()
