# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:40:35 2019

@author: Abhishek
"""

class Piggy_Bank:
    '''Piggy Bank Class supports Deposit Withdraw and Balance check'''
    def __init__(self):
        self.balance = 0
        self.tempAmount = 0
    
    def Start(self):
        str = "Start";
        inp = "";
        print(str.center(50, '-'))
        inp = input("Start or End:");
        while inp != "End":
            operation = input("Add ,Withdraw or Check :")
            if(operation == "Add"):
                self.tempAmount = int(input("Add Amount:"))
                self.Add(self.tempAmount)
                print("After adding, your updated balance is {0:.1f} rupees".format(self.Check()))
                inp = input("Start or End:");
            elif operation == "Withdraw":
                self.tempAmount = int(input("Withdraw Amount:"))
                self.Withdraw(self.tempAmount)
                print("After withdraw, your updated balance is {0:.1f} rupees".format(self.Check()))
                inp = input("Start or End:");
            elif operation == "Check":
                print("Your current balance is {0:.1f} rupees".format(self.Check()))
                inp = input("Start or End:");
                
    def Add(self, amount):
        self.balance += amount
    
    def Withdraw(self, amount):
        if(self.Check() > amount):
            self.balance -= amount
        else :
            print("UnSufficient Balance")
    
    def Check(self):
        return self.balance