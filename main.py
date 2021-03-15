# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 16:57:57 2021

@author: Kunal
"""

# Full Name, Age, Gender, Mobile Number, Email, BMI, Membership Duration in months (1, 3, 6, or 12)
class Super_User:
    def __init__(self):
        self.member = dict([])
        self.regimen = dict([])
        
    def create_member(self,name,age, gender, mobile_num, email, BMI, membership_dur):
        self.member[mobile_num] = {}
        self.member[mobile_num]["name"] = name
        self.member[mobile_num]["age"] = age
        self.member[mobile_num]["gender"] = gender
        self.member[mobile_num]["mobile_num"] = mobile_num
        self.member[mobile_num]["email"] = email
        self.member[mobile_num]["BMI"] = int(BMI)
        if membership_dur==3 or membership_dur==1 or membership_dur==6 or membership_dur==12:
            self.member[mobile_num]["membership_dur"] = int(membership_dur)
        else:
            self.member[mobile_num]["membership_dur"] = 1
        
    def view_member(self):
        for i in self.member.keys():
            print("Name :",self.member[i]["name"])
            print("age :",self.member[i]["age"])
            print("Gender :",self.member[i]["gender"])
            print("Mobile Numer :",self.member[i]["mobile_num"])
            print("Email :",self.member[i]["email"])
            print("BMI :",self.member[i]["BMI"])
            print("Membership Duration :",self.member[i]["membership_dur"])
#     def view_all-member(self):
        
        
    def delete_member(self,mobile_num):
        return self.member.pop(mobile_num)   
    def update_member(self,mobile_num,membership_dur):
        self.member[mobile_num]["membership_dur"] = int(membership_dur)
        
    def create_regimen(self,BMI):
        self.regimen[BMI] = {}
        if BMI<18.5:
            self.regimen[BMI]["Mon"] = "Chest"
            self.regimen[BMI]["Tue"] = "Biceps"
            self.regimen[BMI]["Wed"] = "Rest"
            self.regimen[BMI]["Thu"] = "Back"
            self.regimen[BMI]["Fri"] = "Triceps"
            self.regimen[BMI]["Sat"] = "Rest"
            self.regimen[BMI]["Sun"] = "Rest"
        elif BMI<25:
            self.regimen[BMI]["Mon"] = "Chest"
            self.regimen[BMI]["Tue"] = "Biceps"
            self.regimen[BMI]["Wed"] = "Cardio/Abs"
            self.regimen[BMI]["Thu"] = "Back"
            self.regimen[BMI]["Fri"] = "Triceps"
            self.regimen[BMI]["Sat"] = "Legs"
            self.regimen[BMI]["Sun"] = "Rest"
        elif BMI<30:
            self.regimen[BMI]["Mon"] = "Chest"
            self.regimen[BMI]["Tue"] = "Biceps"
            self.regimen[BMI]["Wed"] = "Abs/Cardio"
            self.regimen[BMI]["Thu"] = "Back"
            self.regimen[BMI]["Fri"] = "Triceps"
            self.regimen[BMI]["Sat"] = "Legs"
            self.regimen[BMI]["Sun"] = "Cardio"
        elif BMI>=30:
            self.regimen[BMI]["Mon"] = "Chest"
            self.regimen[BMI]["Tue"] = "Biceps"
            self.regimen[BMI]["Wed"] = "Cardio"
            self.regimen[BMI]["Thu"] = "Back"
            self.regimen[BMI]["Fri"] = "Triceps"
            self.regimen[BMI]["Sat"] = "Cardio"
            self.regimen[BMI]["Sun"] = "Cardio"

    def view_regimen(self):
        return self.regimen
    def del_regimen(self,BMI):
        return self.regimen.pop(BMI)
    def update_regimen(self,BMI,week_no,value):
        week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
        self.regimen[BMI][week[week_no-1]] = value
            
class User:
    def __init__(self, member, regimen, phn):
        self.myprofile = member[phn]
        self.myregimen = regimen
        self.phn = phn
    def view_myprofile(self):
        return self.myprofile
    def view_myregimen(self):
        return self.myregimen[self.myprofile['BMI']]


A = Super_User()
opt = True
while(opt == True):
    print("Do you want to enter as User or Super User")
    print("For user Press 1 and For Super user Press 2")
    val = int(input())
    if val == 1:
        sup = True
        print("Congrats for Success full Login ans Super User!!")
        while(sup == True):
            if bool(A.member) == False:
                name = input("Enter Name: ")
                age  = input("Enter Age: ")
                gender = input("Enter gender: ")
                mob = input("Enter mob: ")
                email = input("Enter email")
                BMI = int(input(" Enter BMI: "))
                mem_dur = input("Enter Membership duration: ")
                A.create_member(name, age,gender, mob, email, BMI, mem_dur)
                A.create_regimen(BMI)
            print("1> Create Member,\n2> View Member,\n3> Delete Member,\n4> Update Member,\n5> Create Regimen,\n6> View Regimen,\n7> Delete Regimen,\n8> Update Regimen")
            num = int(input())
            if num == 1:
                name = input("Enter Name: ")
                age  = input("Enter Age: ")
                gender = input("Enter gender: ")
                mob = input("Enter mob: ")
                email = input("Enter email")
                BMI = int(input(" Enter BMI: "))
                mem_dur = input("Enter Membership duration: ")
                A.create_member(name, age,gender, mob, email, BMI, mem_dur)
            elif num == 2:
                print(A.view_member())
            elif num == 3:
                mobile_num = input("Enter the mobile no for the user which should be deleted!!")
                A.delete_member(mobile_num)
            elif num == 4:
                mobile_num = input("Enter the mob no to be updated")
                membership_dur = int(input("Enter the duration upto which you want to extend to terminate \nChoose months between 1,3m6 or 12 only else 1 will be selected \npress 0 to terminate"))
                try:
                    A.update_member(mobile_num,membership_dur)
                except:
                    print("Invalid User Details Enter Again")
            elif num == 5:
                create_reg = int(input("Enter The BMI Index for creating the regiment"))
                A.create_regimen(create_reg)
            elif num == 6:
                print(A.view_regimen())
            elif num == 7:
                mob_num = input("Enter the mob number you want to delete")
                try:
                    A.delete_member(mob_num)
                except:
                    print("Invalid Number")
            elif num == 8:
                create_reg = int(input("Enter The BMI Index for updating the regiment"))
                week = input("Enter the week from 1-7 corresponding Mon to Sun")
                value = input("Enter the value of regimen")
                try: 
                    A.update_regimen(create_reg, week, value)
                except:
                    print("Invalid User Details")
            else:
                print("INvalid Input!!")
            print("Want to Enter More Y/n!!")
            sup = input() == 'Y'
    elif val == 2:
        user1 = True
        print("Congrats you are a User Now!!")
        while(user1 == True):
            phn = input("Enter the phn number")
            try:
                B = User(A.member,A.regimen,phn)
                print("Select any of the following\n 1> View MyRegimen \n2> View My Prifile")
                val = int(input())
                if val == 1:
                    print(B.view_myregimen())
                elif val == 2:
                    print(B.view_myprofile())
                else:
                    print("Wrong Choice!!")
            except:
                print("Pls create User for corresponding credentials")
            user1 = input("Want to Enter more Y/n!!") == 'Y'
               
               
            
                