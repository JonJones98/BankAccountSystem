from ctypes import alignment
from http import client
from posixpath import abspath
from random import randint, random, randrange
from time import altzone
from numpy import AxisError
import random

class User:
    def __init__(self,first_name,last_name,age,balance):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.account=balance

    def greeting(self):
        print(f'Hello {self.first_name} {self.last_name}!')
        return self
    def make_deposit(self,amount):
        if amount==-1:
            amount=float(input("Enter amount to deposit: $"))
        self.account += amount
        print(f"Deposited {amount},current balance is {self.account}")
        return self
    def make_withdrawal(self, amount):
        if amount==-1:
            amount=float(input("Enter amount to withdrawal: $"))
        self.account -= amount
        print(f"${amount} was withdrawled from your account, current balance is ${self.account}")
        return self
    def display_user_balance(self):
        print(f"Your current balance is {self.account}")
        return self
    def tranfer_money(self,profiles,one,amount):
        two=True
        while two:
            if amount==-1:
                amount=float(input("Tranfer amount: $"))
            tranfer_id=int(input("What is the ID of the account you want to tranfer to? "))
            try:
                profiles[s_profile[tranfer_id]]
                match=1
            except:
                print("Opps.... Id name not found. Try again")
                match=0
            if match==1:
                user_receive=profiles[s_profile[tranfer_id]]
                user_receive.account += amount
                self.account -= amount
                print(f"${amount} was tranfered to {user_receive.first_name}. Your current balance is ${self.account}")
                two=False
        return self
    def yeild_interest(self):
        APY=self.account*.40
        self.account += APY
        print(f"Interest Occurred: ${APY}")
        return self

profiles={}
tasks=["(1) Make a deposit","(2) Withdraw funds","(3) Check balance","(4) Tranfer funds","(5) Quick Deposit and Withdrawl","(6) Logout"]

def p():
    print("Goodbye!!")
def c(one):
    c=input(":")
    if c=="m":
        one=False
        return

history=[]
def new_user():
    history.append(master_list)
    del master_list[:]
    Master_Dictionary.clear()
    new_person=input("First name:")
    new_person_last=input("Last name:")
    new_person_age=int(input("Age:"))
    master_list.append(new_person)
    master_list.append(new_person_last)
    master_list.append(new_person_age)
    master_list.append(0)
    if len(Master_Dictionary)==0:
        d=1
    else:
         d=len(Master_Dictionary)+1
    for num in range(0,d):
        if num==d-1:
            if len(history)>=1:
                acc_num=int(randrange(1000,9999))
                Master_Dictionary.setdefault(int(acc_num),master_list)
            if len(history)<1:
                acc_num=int(randrange(1000,9999))
                Master_Dictionary.setdefault(int(acc_num),master_list)
    s_profile.setdefault(int(acc_num),master_list[0])
    launch=acc_num
    verification(Master_Dictionary,launch)
    print("Thanks, for creating an account with us today!!! Your Account ID is : ",acc_num)

def verification(Master_Dictionary,launch):
    check=(Master_Dictionary.get(launch))
    afn=None
    aln=None
    aag=None
    aba=None
    for ver in check:
        if afn== None:
            afn=ver
        elif aln== None:
            aln=ver
        elif aag== None:
            aag=int(ver)
        elif aba==None:
           aba=int(ver)
    client=User(afn,aln,aag,aba)
    profiles[s_profile[launch]]=client

Master_Dictionary = {}
s_profile ={}
master_list=[]
system=True
while system:
    amount=-1
    print("Login, New User, or Close Window ?")
    print("Type: 'l' to Login , 'n' to create account or 'c' to Exit")
    x=input(': ')
    if x =="c":
        system=False
        p()
        break
    if x =="n":
        new_user()
    launch=int(input("Account ID: "))
    if launch =="close":
        system=False
        p()
    try:
        profiles[s_profile[launch]]
        #verification(Master_Dictionary,launch)
        good=1
    except:
        print(profiles)
        print("Incorrect Account ID. Try again")
        continue
        
    if good ==1:
        #verification(Master_Dictionary,launch)
        user_id=profiles[s_profile[launch]]
        user_id.greeting()
        run=True
        while run:
            for t in tasks:
                print(t)
            task=input("Type Numeric Value to continue: ")
            if task == "1":
                one=True
                while one:
                    user_id.make_deposit(amount)
                    print("Main Menu (m) or Make another deposit (d)")
                    c=input(":")
                    if c=="m":
                        one=False  
            elif task == "2":
                one=True
                while one:
                    user_id.make_withdrawal(amount)
                    print("Main Menu (m) or Make another withdrawl (w)")
                    c=input(":")
                    if c=="m":
                        one=False
            elif task == "3":
                one=True
                while one:
                    user_id.yeild_interest().display_user_balance()
                    print("Exit to Main Menu (m) or Refresh (r)?")
                    c=input(":")
                    if c=="m":
                        one=False
            elif task == "4":
                one=True
                while one:
                    user_id.tranfer_money(profiles,one,amount)
                    print("Main Menu (m) or Make another transfer (d)")
                    c=input(":")
                    if c=="m":
                        one=False
            elif task == "5":
                if launch == "Jake":
                    user_id.make_deposit(20).make_deposit(30).make_deposit(40).make_withdrawal(15).yeild_interest().display_user_balance()      
                if launch == "Jonathan":
                    user_id.make_deposit(1200).make_deposit(1200).make_withdrawal(900).make_withdrawal(50).make_withdrawal(20).make_withdrawal(10).yeild_interest().display_user_balance()      
            elif task == "6":
                run=False
    