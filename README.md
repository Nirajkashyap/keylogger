
Python Keylogger for Windows
====================================
Coded By: Niraj kashyap

STEP 1: preparing  PYTHON SCRIPT ||

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

STEP 2 : PREPARING .EXE FROM PYTHON SCRIPT basic requirement  ||

include setup.py file in your current script directory

description of setup.py file:
import py2exe lib to build exe from .py file and include distcore util for windows enviroment 


STEP 3: PREPARING .EXE FROM PYTHON SCRIPT ||
run this command in your PYTHON ide in current workspace("directory")

"python setup.py py2exe"

Two directories will be created when you run your setup script, build and dist.
The build directory is used as working space while your application is being packaged.
It is safe to delete the build directory after your setup script has finished running.
The files in the dist directory are the ones needed to run your application.

dist directory is your main directory where your exe is bulided and named by your script name i.e here ( keylog.py --> keylog.exe)

STEP 4: MAKING dist DIRECTORY TO YOUR FINAL APPILACTION BY WINRAR APPLICATION.
THIS STEP INCLUDE SOME BASIC STEP IN WINRAR APPLIACTION .
YOU HAVE TO CREATE WINRAR OF CURRENT DIST FOLDER AND THEN MAKE SOME SFX CHANGE TO MAKE THAT WINRAR TO APPLICATION 
SNAPSHOT FOR THAT IS INCLUDE WITH THIS GIT 
