from distutils.command.config import config
from random import randint
from tkinter import *
from PIL import Image,ImageTk

# main window
root=Tk()
root.title("Rock Paper Scissor") #set title to our window
root.configure(background="#9b59b6") #set background to window using config

# creating picture variables and opening them using Pillow
rock_img=ImageTk.PhotoImage(Image.open("rock.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper_com.jpg"))
scisssor_img=ImageTk.PhotoImage(Image.open("scissor.png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissor_comp.png"))

#inserting the picture
user_label=Label(root,image=paper_img,bg="#9b59b6")                  #created user and comp variables  
comp_label=Label(root,image=paper_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=4)                                       #insert the position of images
user_label.grid(row=1,column=0)

#scores
playerscore=Label(root,text='0',font=200,bg="#9b59b6",fg="white")            #created user and comp variables
computerscore=Label(root,text='0',font=200,bg="#9b59b6",fg="white")          
computerscore.grid(row=1,column=3)                                           #insert the position of scores
playerscore.grid(row=1,column=1)
#update user score
def updateuserscore():
    score=int(playerscore['text']) #assigning text field of variable some values
    score+=1
    playerscore['text']=str(score) #playing with attributes of variable
#update comp score
def updatecompscore():
    score=int(computerscore['text'])
    score+=1
    computerscore['text']=str(score)

#INDICATORS FOR SHOWING USER AND COMPUTER
user_indi=Label(root,font=200,text="USER",bg="#9b59b6",fg="white")            #created user and comp variables
comp_indi=Label(root,font=200,text="COMPUTER",bg="#9b59b6",fg="white")
user_indi.grid(row=2,column=0)                                               #insert the position of User and comp
comp_indi.grid(row=2,column=4)

# Message of winning condition
msg=Label(root,font=50,bg="#9b59b6",fg="black")
msg.grid(row=3,column=2)
#update message
def updatemsg(x):
    msg['text']=x

# update choices(changing images as per the choices)
choices=["rock","paper","scissor"]
def updateChoice(x):         
    #FOR COMPUTER
    compchoice=choices[randint(0,2)] #randit function will generate random integer which refers to choices index
    if compchoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img_comp)
    elif compchoice=="scissor":
        comp_label.configure(image=scissor_img_comp)
    #FOR USER
    if x== "rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scisssor_img)
    checkwin(x,compchoice)

# Wining and losing conditions
def checkwin(player,computer):
    if player==computer:
        updatemsg("It's a Tie!!")
    elif player=="rock":
        if computer=="paper":
            updatemsg("You Lose!!")
            updatecompscore()
        else:
            updatemsg("You Win!!")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatemsg("You Lose!!")
            updatecompscore()
        else:
            updatemsg("You Win!!")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatemsg("You Lose!!")
            updatecompscore()
        else:
            updatemsg("You Win!!")
            updateuserscore()
    else:
        pass

# Buttons creation and positioning
rock=Button(root,width=25,height=3,text="ROCK",bg="#FF3E40",fg="black",command=lambda:updateChoice("rock"))
paper=Button(root,width=25,height=3,text="PAPER",bg="#FAD02E",fg="black",command=lambda:updateChoice("paper"))
scissor=Button(root,width=25,height=3,text="SCISSOR",bg="#0ABDE3",fg="black",command=lambda:updateChoice("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

root.mainloop()