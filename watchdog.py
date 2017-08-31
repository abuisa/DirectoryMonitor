import os
from time import gmtime, strftime
import win32file
import win32con
# Diwabah ini untuk warnai Output
from termcolor import colored
from colorama import init

init()

# WORK OK in WINDOWS 10 python 3
# The Original Code is From : http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
## Variable Global 
wrk_dir = os.getcwd() + "\\"


def watch_dir():
	global wrk_dir
	ACTIONS = {
	  1 : "CREATED",
	  2 : "DELETED",
	  3 : "UPDATED",
	  4 : "RENAMED from :",
	  5 : "RENAMED to :"
	}
	# Thanks to Claudio Grondi for the correct set of numbers
	FILE_LIST_DIRECTORY = 0x0001

	path_to_watch = "C:\\"
	hDir = win32file.CreateFile (
	  path_to_watch,
	  FILE_LIST_DIRECTORY,
	  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
	  None,
	  win32con.OPEN_EXISTING,
	  win32con.FILE_FLAG_BACKUP_SEMANTICS,
	  None
	)


	#
	# ReadDirectoryChangesW takes a previously-created
	# handle to a directory, a buffer size for results,
	# a flag to indicate whether to watch subtrees and
	# a filter of what changes to notify.
	#
	# NB Tim Juchcinski reports that he needed to up
	# the buffer size to be sure of picking up all
	# events when a large number of files were
	# deleted at once.
	#
	# Daftar WARNA : 
	## colored : yellow, magenta, cyan, red, blue, white
	
	results = win32file.ReadDirectoryChangesW (
	hDir,
	1024,
	True,
	win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
	 win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
	 win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
	 win32con.FILE_NOTIFY_CHANGE_SIZE |
	 win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
	 win32con.FILE_NOTIFY_CHANGE_SECURITY,
	None,
	None
	)
	for action, file in results:
		full_filename = os.path.join (path_to_watch, file)
		#print( full_filename, ACTIONS.get (action, "Unknown"))
		d0 = ACTIONS.get(action, "Unknown")
		d1 = strftime("%Y-%m-%d %H:%M", gmtime())
		d2 = str(d1 + ' : '+ ACTIONS.get(action, "Unknown") +'\t --> '+full_filename)
		#print (ACTIONS.get(action, "Unknown") +'\t --> '+full_filename)
		write_2file(wrk_dir+'Action.LOG',d2)
		if d0 == "DELETED":
			print(colored(d2,'red'))
		elif d0 == "UPDATED":
			print(colored(d2,'cyan'))
		elif d0 == "CREATED":
			print(colored(d2,'green'))
		elif d0 == "RENAMED from :":
			print(colored(d2,'yellow'))
		else:
			print(colored(d2,'blue'))
			#print(d2)

def write_2file(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
		#f.write(s)
		#print (colored(' Write : "'+s[:12]+'...", to file : '+fl,'green'))
	except:
		f = open(fl,'w')
	f.close
try:
	#while 1:
	while True:		
		try:
			watch_dir()
			#x=input('Nama : ')
			#if x == "x":
			#	break
		except KeyboardInterrupt:
			break
except:
#except: 
	#print("Bey...bey..:)..")
	pass
"""
while True:
	try:		
		watch_dir()
		#x=input('Nama : ')
		#if x == "x":
		#	break
	except KeyboardInterrupt:
	#except: 
		#print("Bey...bey..:)..")
		break
	except:
		break	
"""		