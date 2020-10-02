# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:16:22 2019

@author: Ravi Seethepalli

this py file has the definition of buggy class and is same for each buggy created
there are some class variables and some instance variables
all individual buggy specific details are under the "self"

"""

import datetime
import time
import os

class buggy:
    total_buggy_count=0
    assigned_buggy_count=0
    directory=os.getcwd()
    init_file_name="init.txt"
    c_file_name="buggy.txt"
    project_name="mybuggy"
    # buggies dict this will store the details of buggies created and assigned to, key = buggy ID, value = string of GUGGY NAME< ASSIGNED TO< BATT LEVEL< ASSIGNED TIME
    buggies={}
    
    def __init__(self, bname):
        self.name = bname
        self.bid = buggy.total_buggy_count
        self.status= "Available"
        self.current_location="Loc1"
        self.last_location="Loc0"
        self.batt_level="100"
        self.assigned_to="none"
        self.last_assigned_to="none"
        self.start_time="NA"
        self.end_time="NA"
        buggy.buggies.update({self.bid:""})
        buggy.total_buggy_count= buggy.total_buggy_count+1
        #print("Initializing a new buggy : "+ self.name)
        return
       
    def get_buggy_id(self):
        print(self.bid)
        return
    
    def assign_buggy_to(self,name):
        # function to assign the buggy to an individual, when the buggy is assigned
        # its status is set to not available and the total buggy avaiable is reduced by 1
        if int(self.check_batt_level())>30:
            self.assigned_to=name
            self.last_assigned_to=name
            self.status="NotAvailable"
            self.start_time=datetime.datetime.now().time().strftime('%H:%M:%S')
            buggy.assigned_buggy_count=buggy.assigned_buggy_count+1
            #print("Buggy assigned to :"+self.assigned_to)
            self.write_file()
            currentDT = datetime.datetime.now()
            dstring=str(currentDT.hour)+str(currentDT.minute)+str(currentDT.day)+str(currentDT.month)+str(currentDT.year)
            s=dstring+","+str(self.bid)+","+self.name+","+self.status+","+self.assigned_to+","+self.current_location+","+self.last_assigned_to+","+self.batt_level
            buggy.buggies[self.bid]=s
            self.update_init_file()
        else:
            #print("Batt level is low, need to be rechagred, cannot assign")
            self.status="Not Available"
            pass
        return
    def unassign_buggy(self):
        # function to unassign the buggy and then mark that buggy as available, the assigned buggy count is reduced by 1
        self.assigned_to="NONE"
        self.status="Available"
        buggy.assigned_buggy_count=buggy.assigned_buggy_count-1
        #self.start_time=""
        self.end_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        #print("buggy unassigned")
        self.write_file()
        currentDT = datetime.datetime.now()
        dstring=str(currentDT.hour)+str(currentDT.minute)+str(currentDT.day)+str(currentDT.month)+str(currentDT.year)
        s=dstring+","+str(self.bid)+","+self.name+","+self.status+","+"None"+","+self.current_location+","+self.last_assigned_to+","+self.batt_level
        buggy.buggies[self.bid]=s
        self.update_init_file()
        return
    
    def check_batt_level(self):
        #print("Batt level is :" + str(self.batt_level))
        return self.batt_level
    
    def change_batt_level(self,blevel):
        self.batt_level=blevel
        return
    def change_buggy_name(self,name):
        # on rate occassions if someone want to change the name of the buggy
        self.name=name
        return
    def time_diff(self):
        # calculates the difference between end time and start time of
        #self.start_time=datetime.datetime.now().time().strftime('%H:%M:%S')
        #time.sleep(5)
        #self.end_time=datetime.datetime.now().time().strftime('%H:%M:%S')
      
        #print("2.End Time Sec's: "+ str((self.end_time[6:8])))
        #print("2.Start Time Sec's: "+ str((self.start_time[6:8])))
        #diff = int(self.end_time[6:8]) - int(self.start_time[6:8])
        diff = (datetime.datetime.strptime(self.end_time,'%H:%M:%S') - datetime.datetime.strptime(self.start_time,'%H:%M:%S')) 
        #print(str(diff))
        
        return str(diff)
    
    def write_file(self):
        # this function is called to saved the status of the buggy into a file, if it is first time creating the buggy's then 
        # a new file is opened else an existig file is opened and data appended to it
        #print("inside write file")
        
        path=self.directory+"\/"+ self.c_file_name
        #print(path)
        
        if not os.path.isfile(path):
            
           
            
            f=open(path,'w')
            payload=str(self.name) +"," + str(self.bid) +","+str(self.status) +"," + str(self.assigned_to) +"," + str(self.last_assigned_to) + "," +str(self.start_time) +","+str(self.end_time)+"\n"
            f.write(payload)
        else:
            
            
            
            f=open(path,'a+')
            payload=str(self.name) +"," + str(self.bid) +","+str(self.status) +"," + str(self.assigned_to) +"," + str(self.last_assigned_to) + "," +str(self.start_time) +","+str(self.end_time)+"\n"
            #print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            #print(f.tell())
            #f.seek(0,0)
            f.write(payload)
        f.close()
        '''
        path="D:\\Ravi\\learning\\pyprogfiles\\WebCrawler\\test\\text.txt"
        data="Hi This is Ravi"
        write_file(path,data)
        '''
        return
   # init file is the file where the details of the buggies are stored, this is a back up file
   # in th eenvt of a pc crash the data to restpre the program is stored here.
    def update_init_file(self):
            init_path=self.directory+"\/"+ self.init_file_name    
            if not os.path.isfile(init_path):
            
                f0=open(init_path,'w')
                payload0=str(buggy.buggies)
                #print("creating initialization file")
                f0.write(payload0+"\n")
            
           
            else:
            
                f0=open(init_path,'w')
                payload0=str(buggy.buggies)
                #print("updating initialization file")
                f0.write(payload0+"\n")
         
            f0.close()
             
            return
    
    def print_buggy_count(self):
        print(self.total_buggy_count)
        return

    def set_current_location(self,loc):
        self.current_location=loc
        return
        # this must always be called before setting the current location
    def set_last_location(self):
        self.last_location=self.current_location
        return

'''  
    # creating a buggy by name "Mickey"
buggy1=buggy("Mickey")
#assigining the buggy to "Ravi"
buggy1.assign_buggy_to("Ravi")
# waiting for the buggy to be returned
time.sleep(120)
# unassigning the buggy
buggy1.unassign_buggy()
print("Buggy "+ buggy1.name + " with ID " + str(buggy1.bid) +" is " + str(buggy1.status))
print("Buggy "+ buggy1.name + " with ID " + str(buggy1.bid) +" is last assigned to " + str(buggy1.last_assigned_to))
print("for a period of (hh:mm:ss) "+buggy1.time_diff())
'''

