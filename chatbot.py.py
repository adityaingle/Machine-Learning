from tkinter import *
#import PhotoImage

#create main window

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("MyBot")

conversation = [
    "Good morning",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name",
    "My name is Aditya",
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)


master = Tk()
master.title("ChatBot")
master.geometry("500x650")
img=PhotoImage(file="robot.png")
photo=Label(master, image=img)
photo.pack(pady=5)
frame=Frame(master)
sc=Scrollbar(frame)
msg=Listbox(frame, width=80, height=20)
sc.pack(side=RIGHT, fill=Y)
msg.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF=Entry(master, font=("Verdana", 20))
textF.pack(pady=10)

def ask():
    while True:
        query=textF.get()
        if query=='exit':
            break
        response = chatbot.get_response(query)
        print(response)
        msg.insert(END, "you :" +query)
        msg.insert(END,"bot:")
        msg.insert(END,response)
        textF.delete(1.0,END)
        
button =Button(master,
                   text="ASK",
                   fg="red",
                   command=ask)
button.pack()
# Run forever!
master.mainloop()