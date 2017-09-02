import pyinotify

# Module untuk handle time 
#from time import gmtime, strftime
import datetime
import time

#Modul untuk Warna
from termcolor import colored

## Handle Time 
tm = time.time()
d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')

# Daftar WARNA : 
## colored : yellow, magenta, cyan, red, blue, white

class ShowEvent(pyinotify.ProcessEvent):
    global d1
    def process_IN_ACCESS(self, event):
        print colored(d1+" : ACCESS \t\t:",'magenta'), colored(event.pathname,'magenta')

    def process_IN_ATTRIB(self, event):
        print  d1+" : ATTRIB \t\t:", event.pathname

    def process_IN_CLOSE_NOWRITE(self, event):
        print  d1+" : CLOSE_NOWRITE \t:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        print  d1+" : CLOSE_WRITE \t:", event.pathname

    def process_IN_CREATE(self, event):
        print  colored(d1+" : CREATE \t\t:",'green'), colored(event.pathname,'green')

    def process_IN_DELETE(self, event):
        print  colored(d1+" : DELETE \t\t:",'red'), colored(event.pathname,'red')

    def process_IN_MODIFY(self, event):
        print  colored(d1+" : MODIFY \t\t:",'cyan'), colored(event.pathname,'cyan')

    def process_IN_OPEN(self, event):
        print  d1+" : OPEN \t\t:", event.pathname

    def process_IN_MOVED_FROM(self,event):
        print colored(d1+" : RENAME FROM \t:",'yellow'), colored(event.pathname,'yellow')

    def process_IN_MOVED_TO(self,event):
        print colored(d1+" : RENAME TO \t:",'yellow'), colored(event.pathname,'yellow')
		
#IN_MOVED_FROM       File moved out of watched directory (*)
#IN_MOVED_TO         File moved into watched directory (*)
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
