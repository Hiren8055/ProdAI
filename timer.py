import time
import graphics
from graphics import *
from button import Button
import time
import datetime
import pandas as pd

win1 = graphics.GraphWin("Win_1",400,400)

def win_1(win):
    
    #1
    win1.setCoords(0,0,3,4)
    input_task = Entry(Point(1.45,3.5),25)
    input_task.draw(win1)
    
    #3
    start_button = Button(win1,Point(1.4,2.0),1,1,"Start")
    start_button.activate()
    
    #2
    input_mins = Entry(Point(1.28,3.0),3)
    input_mins.draw(win1)
    input_sec = Entry(Point(1.6,3.0),3)
    input_sec.draw(win1)


    input_task_label=""
    input_mins_label=""
    input_sec_label=""
        

    #while start to get labels
    while input_sec_label=="":
        
        pt = win1.getMouse() 
        input_task_label = input_task.getText()
        input_mins_label = input_mins.getText()
        input_sec_label = input_sec.getText()
            

#-----------------------------PRESSED START BUTTON ----------------------------
    if start_button.clicked(pt):
        
        #all entrys move away
        input_task.move(5,5)
        input_mins.move(5,5)
        input_sec.move(5,5)

        #task labels after entry
        Task_label = Text(Point(1.45,3.5),input_task_label)
        Task_label.draw(win1)

        #if mins is not define take it as zero            
        if input_mins_label =="":
            input_mins_label =0

#-------------------Solve this problem----------------------------------------------------------------            
        if input_sec_label=="" or input_task_label=="":
            start_button = Button(win1,Point(5,5),1,1,"Start")
            Task_label = Text(Point(5,5),input_task_label)
            input_sec =Text(Point(5,5),input_task_label)
            input_mins = Text(Point(5,5),input_task_label)
            input_task =Text(Point(5,5),input_task_label)
            win_1(win1)
            #fun = Text(Point(1.5,0.5),"""What is your problem man!! just write your task above""")
            #fun.draw(win_1) 
        
        
        secs =int(input_sec_label);mins =int(input_mins_label);
        completed_button = Button(win1,Point(1.4,2.0),1,1,"Complete")
        completed_button.activate()


        while mins>=0:
            mins = mins
            seconds = (secs % 60) + mins-1
                
            point = win1.checkMouse()
                
            if point== None:
                pass
            elif completed_button.clicked(point):
                outputdata("completed_early",str(input_task_label),input_sec_label,input_mins_label)
                #Mins_label =Text(Point(1.28,3.0),"0")
                #Mins_label.draw(win1)
                #Sec_label =Text(Point(1.6,3.0),"0")
                #Sec_label.draw(win1)
                Task_label.move(5,5)
                win_1(win1)

            Mins_label=Text(Point(1.28,3.0),mins)
            #Mins_label.setSize(0.5)
            Mins_label.draw(win1)
            Sec_label=Text(Point(1.6,3.0),secs)
            #Sec_label.setSize(0.5)
            Sec_label.draw(win1)
            time.sleep(1)
                
            if secs == 0:
                secs= 59
                mins-=1
            secs -= 1
            Mins_label.move(5,5)
            Sec_label.move(5,5)
    else:
        win_1(win1)
        
    win_2= GraphWin("RED EYE", 1028, 600)
    
    myImage = Image(Point(500,300),'Redeye.gif')
    myImage.draw(win_2)
    
    win_2.getMouse()
    win_2.close()
    
    delay_button = Button(win1,Point(1.4,1),0.5,0.5,"Delay")    
    delay_button.activate()

    p = win1.getMouse()
    
    if delay_button.clicked(p) or completed_button.clicked(p):
        if delay_button.clicked(p):
#----------------------------Clear screen-------------------
                delay_button.deactivate()
                Task_label.move(5,5)
                delay_button.move(5,5)
                outputdata("delayed",str(input_task_label),input_sec_label,input_mins_label)
                win_1(win1)
                print("Delay")

        
        elif completed_button.clicked(p):
#------------------------------Clear screen-----------------------
            delay_button.deactivate()
            Task_label.move(5,5)
            delay_button.move(5,5)
            outputdata("completed",str(input_task_label),input_sec_label,input_mins_label)
            win_1(win1)
            print("Completed")
    else:
        while not delay_button.clicked(p) or not completed_button.clicked(p):
            p = win1.getMouse()
            if delay_button.clicked(p):
#----------------------------Clear screen----------------------------
                delay_button.deactivate()
                delay_button.move(5,5)
                outputdata("delayed",str(input_task_label),input_sec_label,input_mins_label)
                input_task_label=""
                Task_label.move(5,5)
                win_1(win1)
                print("Delay")

        
            elif completed_button.clicked(p):
#---------------------------Clear screen-------------------------
                Task_label = Text(Point(1.45,3.5),"")
                Task_label.draw(win_1)
                delay_button.deactivate()
                delay_button.move(5,5)
                
                outputdata("completed",str(input_task_label),input_sec_label,input_mins_label)
                win_1(win1)
                print("Completed")


#---------------------------IO------------------------------
def outputdata(button,task_name,secsAllotedToTask,minsAllotedToTask):
        df = pd.read_csv("Data.csv")
        t = time.ctime()
        if task_name == "":
            task_name = "None"
        df1 = pd.DataFrame({"Time":[t[11:19]],"Date":[t[8:10]],"Month":[t[4:7]],"Year":[t[20:25]],"weekday":[t[0:3]],"Button":[button],"Task":[task_name],"Minutes":[str(minsAllotedToTask)],"Seconds":[str(secsAllotedToTask)]})
        df = df.append(df1,ignore_index = True)
        df.to_csv("Data.csv")
    
win_1(win1)







def remove_win(win,x,y,*buttons):
    for i in buttons:
        buttons.move(x,y)
    

#def main():
   # win_1()
   # if delay_button.clicked(p):
    #   win_1()
     #  print("Delay")
   # elif completed_button.cliked(p):
    #    win_1("Completed")    
        
#main()    

        



    

