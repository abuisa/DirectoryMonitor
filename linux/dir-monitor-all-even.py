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
    #global d1, # use d1 as global variable not give real time
    def file_event(self,act, event,clr): # ini Experiment
        tm = time.time()	
        d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')
        if not 'ActionsREC.LOG' in event.pathname: # disable baris ini jika gunakan exclude_filter (masih errror) 
            d2 = d1+" : " + act + " \t: " + event.pathname		
            write_2log('ActionsREC.LOG',d2)
            print colored(d2,clr)
		
    def process_IN_ACCESS(self, event):
        self.file_event('ACCESS__EVENT',event,'magenta')

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
    print ('''-------------------------
 input folder to watch, support multi-folder,
 exp : /var/log /home /mnt
-------------------------''')
    path = raw_input("Folder to Watch : ")
    path = path.split()
    #exlist = ['ActionsREC.LOG^','tes.txt^'] ## exclude_filter masih Error, belum bisa digunakan 
    #exclist = pyinotify.ExcludeFilter(exlist)
    
    if path !="":
        # watch manager
        wm = pyinotify.WatchManager()
        #wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True''', exclude_filter=exclist''') # Not Working
        wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True)

        # event handler
        eh = ShowEvent()

        # notifier
        notifier = pyinotify.Notifier(wm, eh)
        notifier.loop()

if __name__ == '__main__':
    main()
