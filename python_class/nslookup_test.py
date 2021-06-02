# -*- conding: utf-8 -*-
#import os
import socket


#print (os.system('nslookup mails.cne.go.kr 168.126.63.1'))


ais = socket.getaddrinfo('mail.cne.go.kr',0,0,0,0)

print(ais)