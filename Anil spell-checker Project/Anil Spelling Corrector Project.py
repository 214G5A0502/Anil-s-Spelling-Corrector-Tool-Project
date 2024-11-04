from textblob import TextBlob
from tkinter import *

def checkSpelling():
    a = text.get()
    b = TextBlob(a)
    correctedText.set("The corrected word is: " + str(b.correct()))

def scroll_text():
    x = welcomeLabel.winfo_x()
    # Check if the text has scrolled out of view
    if x < -toolLabel.winfo_width() - restLabel.winfo_width():
        x = wn.winfo_width()  # Reset to the right end
    
    # Move labels to the left for scrolling effect
    welcomeLabel.place(x=x-4, y=270)  # Decreased scroll speed to -4
    toolLabel.place(x=x + welcomeLabel.winfo_width()-4, y=270)
    restLabel.place(x=x + welcomeLabel.winfo_width() + toolLabel.winfo_width()-4, y=270)

    wn.after(20, scroll_text)  # Increased delay to 20ms for slower scrolling

wn = Tk()
wn.title("Anil Spelling Corrector Tool with Animation")
wn.geometry('600x300')
wn.config(bg='SlateGray1')

text = StringVar(wn)
correctedText = StringVar(wn)

Label(wn, text='Spell Checker', bg='SlateGray1', fg='gray30', font=('Times', 20, 'bold')).place(x=200, y=10)
Label(wn, text='Please enter the word', bg='SlateGray1', font=('calibre', 13, 'normal'), anchor="e", justify=LEFT).place(x=20, y=70)
Entry(wn, textvariable=text, width=35, font=('calibre', 13, 'normal')).place(x=20, y=110)
Label(wn, textvariable=correctedText, bg='SlateGray1', anchor="e", font=('calibre', 13, 'normal'), justify=LEFT).place(x=20, y=140)
Button(wn, text="Check the word", bg='SlateGray4', font=('calibre', 13), command=checkSpelling).place(x=250, y=200)

# Create labels for scrolling text segments
welcomeLabel = Label(wn, text="Welcome to ", font=('calibre', 10), bg='SlateGray1', fg='blue')  # Blue color
toolLabel = Label(wn, text="Anil's Spelling Corrector Tool", font=('calibre', 10, 'bold'), bg='SlateGray1', fg='#D5006D')  # Dark Pink/Rose color
restLabel = Label(wn, text=". Enter a word to see the correct spelling.													 © AnilKumar - All rights reserved.														Follow me on: >>>>>         https://anilkumar214g5a0502portfolio.netlify.app/", font=('calibre', 10), bg='SlateGray1', fg='blue')

# Set the initial position of the labels to start off-screen to the right
welcomeLabel.place(x=wn.winfo_width(), y=270)
toolLabel.place(x=wn.winfo_width() + welcomeLabel.winfo_width(), y=270)
restLabel.place(x=wn.winfo_width() + welcomeLabel.winfo_width() + toolLabel.winfo_width(), y=270)

scroll_text()

wn.mainloop()
