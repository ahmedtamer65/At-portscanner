#colors
# Regular Colors  
Bk="\[\033[0;30m\]" # Black
Rd="\[\033[0;31m\]" # Red
Gr="\[\033[0;32m\]" # Green
yl="\[\033[0;33m\]" # Yellow
Bl="\[\033[0;34m\]" # Blue
Pr="\[\033[0;35m\]" # Purple
Cy="\[\033[0;36m\]" # Cyan
Wh="\[\033[0;37m\]" # White
###############
import socket
import sys
from time import *
from datetime import datetime
####################
####################
#USE==> python to run...#
#Coded By AhmedTamer (scar). #
#https://t.me/OsTaZ_3aLaMy #
####################
####################
ip=input ("===> ENTER YOUR IP TO START: ")
t1=datetime.now()
print("Scanning Start.. %s Please Wait.. "%ip)
sleep(1)
####################
try:
    for port in range(1,6553):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(s.connect_ex((ip,port))==0):
            try:
                serv=socket.getservbyport(port)

            except socket.error:
                serv="Unknown Service"
            print ("Port %s Open Service:%s "%(port,serv))
        t2=datetime.now()
        t3=t2-t1
    print ("Scanning Completed On %s"%t3)
    print ("scar")
except KeyboardInterrupt:
    print(gr+"By :AhmedTamer(scar)")
    print(rd+"See You Soon...!")
###############################

