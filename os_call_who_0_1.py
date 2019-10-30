#!/usr/bin/python3

# -*- coding: utf-8 -*-
# File os_call_who.py
# v0.1
# MGB 19/10/29
# Get details of who is Logged in to the Pi
# 


import subprocess
users=[]

out=subprocess.Popen(['who','-u'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

stdout,stderr=out.communicate()
print (stdout.decode('utf-8'))
print ('error No.',stderr)
tempL=[]

tempS=stdout.decode('utf-8').split("\n")
userNo=len(tempS) - 1

for loop in range(userNo):
    
    tempL = tempS[loop]
   
    tempL=tempL.split()

    users.append(tempL)
    

print('Users: ',users)

for n,eachid in enumerate(users):
    print('User ID ',n,eachid[0],eachid[6])
    
print('\n \n')
print (users[0][0])
    