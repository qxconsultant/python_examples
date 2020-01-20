# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:07:38 2020

@author: qxie
"""

livedoid = input("Do you have Livedoid skin rash? (Yes or No?) ")
if livedoid == "Yes":
    bodytemp = input("Body Temp: ")
    if bodytemp.isnumeric():
        if float(bodytemp) >= 38:
            print("yes")
        else:
            CRP = input("CRP: ")
            if CRP.isnumeric():
                if float(CRP) >= 5:
                    print("yes2")
                else:
                    print("low-risk")
            else:
                print ("invalid")
                exit (1)
    else:
        print ("invalid")
        exit (1)
        
elif livedoid == "No":
    print("ToDo")
else:
    print("invalid")
