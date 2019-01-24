import os
os.system("chmod 777 tools/cutter.py")
os.system("chmod 777 tools/hack.py")
os.system("chmod 777 tools/cphack.py")
os.system("chmod 777 tools/scanner.py")
 
 print ("   [1] scan connecters      [2] cut net to connecters")
 print ("   [3] hack G-mail account  [4] open port to hack  ")






x = str(raw_input("[*] Enter your choice : "))


if x == 1 :
	os.system("python tools/scanner.py")


elif x == 2 :
		os.system("python tools/cutter.py")


elif x == 3 :
		os.system("python tools/hack.py")

elif x == 4 :
		os.system("python tools/cphack.py")		
		


