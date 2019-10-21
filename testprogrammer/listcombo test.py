from guizero import *
import random

l1=[[1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,9,10],
    [1,2,3,4,5,6,7,8,9,10]]


l2=[]
answer_no=0

for x in range(100):
    number1 = random.randint(1,len(l1))
    length1 = len((l1[(number1-1)]))
    number2 = random.randint(1,length1)
    l2.append([number1,number2])


    

class multiplication(object):
    def __init__(self):
        self.app=App()
        self.box1=Box(self.app,layout = "grid")
        self.number1_field=Text(self.box1,grid=[1,1],align="right",size=30,visible=False)
        self.number2_field=Text(self.box1,grid=[3,1],size=30,align="left",visible=False)
        self.start=PushButton(self.box1, grid=[1,2,2,1],visible=True, text="Start",command=self.start)
        self.counter=0
        self.correct=0
        self.wrong=0
        self.correct_text=Text(self.box1, grid=[1,0],visible=False)
        self.wrong_text=Text(self.box1, grid=[2,0], visible=False)
        self.time=Text(self.box1,grid=[3,0],visible=False)
        self.percent_text=Text(self.box1, grid=[4,0],visible=True) 
        self.remaining=Text(self.box1, grid=[0,0], text="99 tilbage", visible=False)
        self.dont_know=PushButton(self.box1, grid=[1,2],visible=False, text="jeg ved det ikke...", command=self.cont)
        self.answer=TextBox(self.box1,grid=[4,1], visible=False, command=self.answer_given)
    
    def start(self):
        self.counter+=1
        self.number1_field.value=l2[self.counter][0]
        self.number2_field.value="* {0}".format(l2[self.counter][1])
        self.correct_val=0
        self.wrong_val=0
        self.time_val=0
        self.percent_val=0
        self.number1_field.show()
        self.number2_field.show()
        self.start.hide()
        self.dont_know.show()
        self.remaining.show()
        self.answer.show()
        self.answer.focus()
        self.answer_no=0
        self.key1=0
        self.correct_answer=0
        self.value1=int(float(l2[self.counter][0]))
        self.value2=int(float(l2[self.counter][1]))
        self.correct_answer=(self.value1*self.value2)
        print(self.correct_answer)
        
        
    def cont(self):
        self.answer.focus()
        self.answer.value=""
        self.counter+=1
        self.percent=(self.correct/(self.counter-1))*100
        self.percent_text.value=self.percent
        self.number1_field.value=l2[self.counter][0]
        self.number2_field.value="* {0}".format(l2[self.counter][1])
        self.remaining.value="{0} tilbage".format(100-self.counter)
        self.value1=int(float(l2[self.counter][0]))
        self.value2=int(float(l2[self.counter][1]))
        self.correct_answer=(self.value1*self.value2)
        print(self.correct_answer)

        
    def answer_given(self,key):
        self.answer.destroy()
        self.answer=TextBox(self.box1,grid=[4,1], visible=True, command=self.answer_given)
        self.answer.focus()
        print("correct answer is ")
        print (self.correct_answer)
        print("you pressed")
        key = int(float(key))
        print (key)
        if self.answer_no==0:
            if int(key)==int(self.correct_answer):
                print("RIGTIGT")
                self.correct+=1
                self.answer_no=0
                self.answer.value=""
                self.cont()
                
            else:
                self.key1=key
                self.answer_no=1
        elif self.answer_no==1:
            print("2. knap trykket")
            print(self.key1+key)
            now_key=self.key1*10+key
            print(now_key)
            if now_key==int(self.correct_answer):
                print("RIGTIGT")
                self.answer.value=""
                self.correct+=1
                self.answer_no=0
                self.cont()
            else :
                print("FORKERT")
                self.wrong+=1
                self.answer_no=0
                self.cont()

game=multiplication()



