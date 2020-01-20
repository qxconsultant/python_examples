# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 00:07:38 2020

@author: qxie
"""

livedoid = input("Livedoid skin rash (Yes or No)? ")
if livedoid == "Yes":
    bodytemp = input("Body Temp: ")
    if bodytemp.isnumeric():
        if float(bodytemp) >= 38:
            ADA2 = input("ADA2 pathogenic mutations: ")
            if ADA2 in [0, 1, 2]:
                if int(ADA2) == 0:
                    print("low-risk")
                elif int(ADA2) == 1:
                    print("medium-risk")
                elif int(ADA2) == 2:
                    print("high-risk")
            else:
                print("invalid")
                exit(1)
        elif float(bodytemp) < 38:
            CRP = input("CRP (mg/dL): ")
            if CRP.isnumeric():
                if float(CRP) >= 5:
                    ADA2 = input("ADA2 pathogenic mutations: ")
                    if ADA2 in [0, 1, 2]:
                        if int(ADA2) == 0:
                            print("low-risk")
                        elif int(ADA2) == 1:
                            print("medium-risk")
                        elif int(ADA2) == 2:
                            print("high-risk")
                else:
                    print("low-risk")
            else:
                print("invalid")
                exit(1)
    else:
        print("invalid")
        exit(1)
elif livedoid == "No":
    neuro = input("Neurological disorder (Yes or No)? ")
    if neuro == "Yes":
        bodytemp = input("Body Temp: ")
        if bodytemp.isnumeric():
            if float(bodytemp) >= 38:
                ADA2 = input("ADA2 pathogenic mutations: ")
                if ADA2 in [0, 1, 2]:
                    if int(ADA2) == 0:
                        print("low-risk")
                    elif int(ADA2) == 1:
                        print("medium-risk")
                    elif int(ADA2) == 2:
                        print("high-risk")
                else:
                    print("invalid")
                    exit(1)
            else:
                CRP = input("CRP (mg/dL): ")
                if CRP.isnumeric():
                    if float(CRP) >= 5:
                        ADA2 = input("ADA2 pathogenic mutations: ")
                        if ADA2 in [0, 1, 2]:
                            if int(ADA2) == 0:
                                print("low-risk")
                            elif int(ADA2) == 1:
                                print("medium-risk")
                            elif int(ADA2) == 2:
                                print("high-risk")
                        else:
                            print("invalid")
                            exit(1)
                    else:
                        print("low-risk")
                else:
                    print("invalid")
                    exit(1)
        else:
            print("invalid")
            exit(1)
    elif neuro == "No":
        print("low-risk")
    else:
        print("invalid")
        exit(1)
else:
    print("invalid")
    exit(1)
