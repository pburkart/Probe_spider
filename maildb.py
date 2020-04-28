import os

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def maildb():
    emailaddress=input(C+"Enter the Email Address (Eg:test@gmail.com): "+W)
    if  ("@" and ".com") or ("@" and ".in") in emailaddress:
        print ( W + '[+]' + G + "Data Breaching....." + '\n'+W)
        os.system("h8mail -t "+emailaddress+" -o src/output.csv > src/log")
        f=open("src/output.csv","r")
        line=f.readlines()
        if len(line) > 1:
            for i in line:
            	print(i)
        else:
            print(G+"E-Mail not found in data breaches")
    else:
        print(R+"Error: Invalid Email Address")
