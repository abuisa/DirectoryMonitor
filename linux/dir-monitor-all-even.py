import pyinotify

# Module untuk handle time 
#from time import gmtime, strftime
import datetime
import time


## Handle Time 
tm = time.time()
d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')


class ShowEvent(pyinotify.ProcessEvent):
    global d1
    def process_IN_ACCESS(self, event):
        print d1+" : ACCESS \t\t:", event.pathname

    def process_IN_ATTRIB(self, event):
        print  d1+" : ATTRIB \t\t:", event.pathname

    def process_IN_CLOSE_NOWRITE(self, event):
        print  d1+" : CLOSE_NOWRITE \t:", event.pathname

    def process_IN_CLOSE_WRITE(self, event):
        print  d1+" : CLOSE_WRITE \t:", event.pathname

    def process_IN_CREATE(self, event):
        print  d1+" : CREATE \t\t:", event.pathname

    def process_IN_DELETE(self, event):
        print  d1+" : DELETE \t\t:", event.pathname

    def process_IN_MODIFY(self, event):
        print  d1+" : MODIFY \t\t:", event.pathname

    def process_IN_OPEN(self, event):
        print  d1+" : OPEN \t\t:", event.pathname

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
