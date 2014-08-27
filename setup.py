 import os
homedir=os.environ['HOME']+"/"
def mkfolder(Cc,Jc):
	os.chdir(homedir)
	hfiles=os.listdir(homedir)
	if "easyExe" not in hfiles:
		os.system("mkdir easyExe")
	ref=homedir+"easyExe"
	os.chdir(ref)
	rfiles=os.listdir(ref)
	if(Cc == True and Jc == True):
		if "java" not in rfiles and "c" not in rfiles:
			os.system("mkdir java c")
		else:
			print "Warning : \"java or c\" course folders already exists."
	elif(Cc == True and Jc == False):
		if "c" not in rfiles:
			os.system("mkdir c")
		else:
			print "Warning : \"c\" course folder already exists."
	else:
		if "java" not in rfiles:
			os.system("mkdir java")
		else:
			print "Warning : \"java\" course folder already exists."
			
	
def genCode(ftype,reffol):
	exef=ftype+"_exe.py"
	os.chdir(homedir+"Desktop/")
	code = """import os,readline
again=True
choice=True

				#--------------------Instructions----------------
print "        --------------------------------------------------------------"
print " """                   '''                    ***EASIER '''+ftype.upper()+''' FILE EXECUTION***'''""" "
print '''
	Instructions:
		1)You've to enter choice to go to your desired directory.
		2)Enter file name(without convention) which you want to run.
		3)Menu will be displayed for further action.
		4)Auto completion feature is available(press <tab> twice).
'''
print '''
	
	Developer :::  Anesh Parvatha,
	N090977, CS 03,
	RGUKT IIIT,Nuzvid.
'''
ftype=\""""+ftype+"""\"
homedir=os.environ['HOME']+'/'
file_path=homedir+"easyExe/"""+ftype+"""/"
#auto completion 
class MyCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  
            if text:  
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  
                 self.matches = [s for s in self.options 
                                    if s and s.endswith("."+ftype)]

        try: 
            return self.matches[state]
        except IndexError:
            return None
# User defined function. To create new file in current directory.
def create_file():
	ls=os.listdir(file_path)
	file_name=raw_input("Enter File Name (without extension):")
	"""
	if ftype=="java":
		nf="""
	b='''public class '''+ file_name +''' {
	public static void main(String args[]) {

	}
}'''
	"""
	elif ftype=="c":
		nf="""
	b='''#include<stdio.h>
main(int argc,char *argv[],char *env[])
{

}'''
	"""
	subcode="""
	while True:
		ft="."+ftype
		file_name+=ft
		if file_name not in ls:
			a1=open(file_path+file_name,"w")
			a1.write(b)
			break
		else:
			print "Warning :File name already exists."
		file_name=raw_input("Enter File Name (without extension):")
	print "New file (",file_name,") created in \'easyExe/"""+ftype+"""\' folder Successfully...!!!"
	"""
	if reffol ==  True:
		fc = """
def path():
	hdir=os.environ['HOME']+"/"
	os.chdir(hdir)
	cl=chr(ord('"""+ftype[0]+"""')-32)
	options='''
	Enter directory for 
		==>"""+ftype+""" Course ["""+chr(ord(ftype[0])-32)+"""/"""+ftype[0]+"""]
		==>Home [H/h]
		==>Desktop [D/d] 
		==>Exit [E/e] ::: '''
	while True:
		choice=raw_input(options)
		# Different paths.
		if (choice=='"""+ftype[0]+"""' or choice==cl):
			os.chdir(hdir+"easyExe/"""+ftype+"""")
			completer = MyCompleter(os.listdir(hdir+"easyExe/"""+ftype+""""))
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab: complete')
			break
		elif (choice=="h" or choice=="H"):
			os.chdir(hdir)
			completer = MyCompleter(os.listdir(hdir))
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab: complete')
			break
		elif (choice=="d" or choice=="D"):
			os.chdir(hdir+"Desktop/")
			completer = MyCompleter(os.listdir(hdir+"Desktop/"))
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab: complete')
			break
		elif (choice == 'e' or choice == 'E'):
			print '''
	Thanks For Run This File..
		'''
			exit(0)
		else:
			print '''
	error: Unknown Path..!!!
			'''
			choice=raw_input(options)
		"""
		fcode = code+nf+subcode + fc
	else:
		fc = """
def path():
	hdir=os.environ['HOME']+"/"
	os.chdir(hdir)
	mes='''
	Enter directory for 
		==>Home [H/h]
		==>Desktop [D/d]
		==>Exit [E/e] ::: '''
	while True:
		choice=raw_input(mes)
		# Different paths.
		if (choice=="h" or choice=="H"):
			os.chdir(hdir)
			completer = MyCompleter(os.listdir(hdir))
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab: complete')
			break
		elif (choice=="d" or choice=="D"):
			os.chdir(hdir+"Desktop/")
			completer = MyCompleter(os.listdir(hdir+"Desktop/"))
			readline.set_completer(completer.complete)
			readline.parse_and_bind('tab: complete')	
			break
		elif (choice == 'e' or choice == 'E'):
			print '''
	Thanks For Run This File..
		'''
			exit(0)
		else:
			print '''
	error: Unknown Path..!!!
			'''
			choice=raw_input(mes)
		"""
		fcode = code+nf+subcode+ fc
	fcc ="""
while again!='e' or again!='E':
	path()
	a=raw_input("Enter File name(without extension): ")
	c=a+"."""+ftype+""""
	"""
	if ftype=="java":
		fcm="""d="javac "+c
	nn=str(os.system(d))
	if len(nn)==1:
		e="java "+a
		os.system(e)"""
	else:
		fcm="""d="gcc -lm -o "+a+" "+c
	nn=str(os.system(d))
	if len(nn)==1:
		e="./"+a
		os.system(e)"""
	filec=fcc+fcm
	rfc="""
	fmenu='''
	
	Enter Your choice 
		==> re-execution [R/r] 
		==> new file [N/n]
		==> main menu [any key]
		==> exit [E/e] ::: '''
	try:
		again=raw_input(fmenu)
	except KeyboardInterrupt:
		print '''
	Warning : Ctrl+c disabled
	'''
	if again=="n" or again=="N":
		create_file()
	while again=='r' or again=='R':
		os.system("clear")
		"""
	if ftype=="java":
		rfcm="""d="javac "+c
		nn=str(os.system(d))
		if len(nn)==1:
			e="java "+a
			os.system(e)"""
	else:
		rfcm="""d="gcc -lm -o "+a+" "+c
		nn=str(os.system(d))
		if len(nn)==1:
			e="./"+a
			os.system(e)"""		
		
	rfcem="""
		try:
			again=raw_input(fmenu)
		except KeyboardInterrupt:
			print '''
		Warning : Ctrl+c disabled
		'''
		if again=="n" or again=="N":
			create_file()
		if again=="e" or again=="E":
			print '''
	Thanks For Run This File..
	'''
			exit(0)
print '''
	Thanks For Run This File..
'''
	"""
	mcode=fcode + filec+rfc+rfcm+rfcem
	wr=open(exef,"w")
	wr.write(mcode)
def setDir(Ccourse,Jcourse):
		while True:
			try:
				dire = raw_input("\nWant to create \"Course\" folders in "+homedir+" directory [y/n] ::: ")
				if (dire == 'y' or dire == 'Y'):
					if (Ccourse == True and Jcourse == True):
						print "setuping both with folders"
						mkfolder(True,True)
						genCode("c",True)
						genCode("java",True)
					elif (Ccourse == True and Jcourse == False):
						print "setuping C only with folders"
						mkfolder(True,False)
						genCode("c",True)
					else:
						print "setuping Java only with folders"
						mkfolder(False,True)
						genCode("java",True)
					break
				elif (dire == 'n' or dire == 'N'):
					if (Ccourse == True and Jcourse == True):
						print "setuping both"
						genCode("c",False)
						genCode("java",False)
				
					elif (Ccourse == True and Jcourse == False):
						print "setuping C only"
						genCode("c",False)
					else:
						print "setuping Java only"
						genCode("java",False)
					break
				else:
					print "\nerror : Invalid entry given."
			except ValueError:
				print "\nerror : Invalid entry given."
			except KeyboardInterrupt:
				print "\n\nWarning : Ctrl+c disabled."
print "\t--------------------------------------------------------------\n\n\t\t***EXECUTION ENVIRONMENT***\t\n\n\tInstructions:\n\t\t1)You've to enter number of courses which you wanna setup.\n\t\t2)Enter your choice to create course folder(s).\n\t\t3)Based on given instructions python file(s) will generate.\n\t\t4)Run your desired file to execute c/java files easily.\n\n"
print "\n\n\tDesigner :::  Anesh Parvatha\n\tN090977,CSE 03\n\tRGUKT IIIT,Nuzvid.\n\n"
print "\t\t------------------------------------------------------"
print "\n\n\t\tJAVA EXECUTION\t[ 1 ]\n\t\tC EXECUTION\t[ 2 ]\n\t\tBOTH\t\t[ 3 ]\n\n"
while True :
	try:
		exe=int(raw_input("\nEnter which one you want to setup ::: "))
		if exe == 1 :
			setDir(False,True)
			break
		elif exe == 2:
			print "C setup"
			setDir(True,False)
			break
		elif exe == 3:
			setDir(True,True)
			break
		else:
			print "\nerror : Invalid entry given."
	except ValueError:
		print "\nerror : Invalid entry given."
	except KeyboardInterrupt:
		print "\n\nWarning : Ctrl+c disabled."	
