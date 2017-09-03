import os
import win32file
import win32con
# Diwabah ini untuk warnai Output
from termcolor import colored
from colorama import init
# Module untuk handle time 
import datetime
import time

init()

# WORK OK in WINDOWS 10 python 3
# The Original Code is From : http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html

## Variable Global 
wrk_dir = os.getcwd() + "\\"

def watch_dir(path_to_watch):
	global wrk_dir
	ACTIONS = {
	  1 : "CREATED",
	  2 : "DELETED",
	  3 : "UPDATED",
	  4 : "REN from",
	  5 : "REN to"
	}
	FILE_LIST_DIRECTORY = 0x0001

	hDir = win32file.CreateFile (
	  path_to_watch,
	  FILE_LIST_DIRECTORY,
	  win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
	  None,
	  win32con.OPEN_EXISTING,
	  win32con.FILE_FLAG_BACKUP_SEMANTICS,
	  None
	)

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
	# Daftar WARNA : yellow, magenta, cyan, red, blue, white	
	
	for action, file in results:
		full_filename = os.path.join (path_to_watch, file)
		if not "ActionsREC.LOG" in full_filename:
			d0 = ACTIONS.get(action, "Unknown")
			## Handle Time 
			tm = time.time()
			d1 = datetime.datetime.fromtimestamp(tm).strftime('%d-%m-%Y %H:%M:%S')
			d2 = d1 + ' : '+ ACTIONS.get(action, "Unknown") +'\t --> '+full_filename
			write_2file(wrk_dir+'ActionsREC.LOG',d2)
			if d0 == "DELETED":
				print(colored(d2,'red'))
			elif d0 == "UPDATED":
				print(colored(d2,'cyan'))
			elif d0 == "CREATED":
				print(colored(d2,'green'))
			elif d0 == "REN from :":
				print(colored(d2,'yellow'))
			else:
				print(colored(d2,'yellow'))


def write_2file(fl,s):
	try:
		f = open(fl,'a+')
		f.write(s+"\n")
	except:
		f = open(fl,'w')
	f.close

try:
	print ("""-------------------------
 input folder to watch
 exp_1 : C:\\Users\\UserName D:\\
 exp_2 : D:\\ 
------------------------- """)
	path = input('Folder to Watch : ')
	if path == "" or path == "x" or path == "X":
		pass
		exit()

	#while 1:
	while True:		
		try:
			watch_dir(path)
		except KeyboardInterrupt:
			break
except:
	pass
	