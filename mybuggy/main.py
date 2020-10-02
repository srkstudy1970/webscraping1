# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 08:39:58 2019

@author: Ravi
"""

from buggy import buggy
import time

print("Welcome to Buggy App")
print(buggy.total_buggy_count)
c=buggy.total_buggy_count
'''
if c :
   print("Buggies have been allocated")
   pass
else:
   print("pls allocate following buggies")


print("Main Program starts from here")
'''

#print(buggy.buggies)
buggy1=buggy("Mickey")
buggy1.assign_buggy_to("Ravi")
#print("Buggy Ravi ID is " +str(buggy1.bid))

buggy2=buggy("Donald")
buggy2.assign_buggy_to("Shakib")
#time.sleep(120)
buggy1.unassign_buggy()
#time.sleep(60)
buggy2.unassign_buggy()
#print(buggy.buggies)

buggy1.assign_buggy_to("Krishna")
#print("Buggy assigned to Krishna ID is " +str(buggy1.bid))


print("Total Buggies : " + str(buggy.total_buggy_count))
print("Assigned Buggies : "+ str(buggy.assigned_buggy_count))
print("Available Buggies count : " + str(buggy.total_buggy_count-buggy.assigned_buggy_count))
print(buggy.buggies)

print(buggy.total_buggy_count)

def show_available_buggies():
    
    '''
    look into the buggies dict values, if there is a "Available" then get the buggy name and buggy id
    '''
    buggy_name=buggy
    print("Buggy "+buggy_name+"is Available")
    return


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def setup_single_buggy(name):
    buggy_id=buggy.total_buggy_count
    print(buggy_id)
    
    return
def setup_buggies_in_bulk(num,names):
    # create buggy objects
    buggies=[]
    for i in range(0,num):
        buggy_id=buggy.total_buggy_count+1
        #print(buggy_id)
        #print(names[i])
        buggy_id=buggy(names[i])
        buggies.append(buggy_id)
    return buggies

names=("Mickey", "Donald","Goffy")
buggies=setup_buggies_in_bulk(len(names),names)

def assign_buggy(buggies,name):
    #print("inside assign_buggy")
    #print("length of buggies : " + str(len(buggies)))
    
    for i in range(0,len(buggies)):
        #print("inside for"+str(i))
        #print("printing buggy name : "+buggies[i].status)
        if buggies[i].status=="Available" and int(buggies[i].batt_level)>30 :   
            buggies[i].assign_buggy_to(name)
            break
        
        else:
            print("No Buggy available")
            pass
    return

def unassign_buggy(buggies,name):
    print("Inside unassign")
    for i in range(0,len(buggies)):
        print("inside for"+str(i))
        print("printing buggy name : "+buggies[i].assigned_to)
        if buggies[i].assigned_to==name :   
            buggies[i].unassign_buggy()
            break
        else:
            print("No Buggy to unassign")
            pass
    
    return
def show_available_buggies(buggies):
    for i in range(0,len(buggies)):
        print(buggies[i].name)
    return buggies

print(show_available_buggies(buggies))
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

